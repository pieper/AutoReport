"""
generate_report.py

Reads topic markdown files from topics/, uses Gemini with built-in Google Search
grounding to research each topic, and writes timestamped reports to reports/.
Updates README.md with a run summary including per-topic change highlights.
"""

import os
import re
import glob
import time
import datetime
import requests
from google import genai
from google.genai import types

# Load .env when running locally (no-op in GitHub Actions)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# --- Configuration ---

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing required environment variable: GEMINI_API_KEY")

TOPICS_DIR = "topics"
REPORTS_DIR = "reports"
README_FILE = "README.md"

MODEL = "gemini-2.5-flash-lite"
RETRY_BUFFER_SECS = 5    # extra seconds added on top of the API-suggested delay
RETRY_TIMEOUT_SECS = 3600  # give up after 1 hour
RETRY_BACKOFF_BASE = 30  # starting backoff for non-429 transient errors (seconds)

README_MARKER_START = "<!-- REPORT_LOG_START -->"
README_MARKER_END = "<!-- REPORT_LOG_END -->"

client = genai.Client(api_key=GEMINI_API_KEY)
os.makedirs(REPORTS_DIR, exist_ok=True)


# --- Helpers ---

def _is_transient(error: Exception) -> bool:
    """Return True for errors that are worth retrying (rate limits, overload, network)."""
    msg = str(error)
    return any(code in msg for code in ("429", "500", "502", "503", "504"))


def _retry_delay(error: Exception, backoff: float) -> float:
    """Return how long to wait before the next attempt."""
    match = re.search(r"retryDelay.*?(\d+(?:\.\d+)?)s", str(error))
    if match:
        return float(match.group(1)) + RETRY_BUFFER_SECS
    return backoff


def _gemini(prompt: str) -> str:
    """Call Gemini without search, retrying transient errors for up to RETRY_TIMEOUT_SECS."""
    deadline = time.monotonic() + RETRY_TIMEOUT_SECS
    backoff = RETRY_BACKOFF_BASE
    attempt = 0
    while True:
        attempt += 1
        try:
            return client.models.generate_content(model=MODEL, contents=prompt).text
        except Exception as e:
            remaining = deadline - time.monotonic()
            if _is_transient(e) and remaining > 0:
                delay = min(_retry_delay(e, backoff), remaining)
                print(f"  Transient error (attempt {attempt}): {e}. Retrying in {delay:.0f}s...")
                time.sleep(delay)
                backoff = min(backoff * 2, 300)
            else:
                raise


def _gemini_with_search(prompt: str) -> str:
    """Call Gemini with Google Search grounding, retrying transient errors for up to RETRY_TIMEOUT_SECS."""
    deadline = time.monotonic() + RETRY_TIMEOUT_SECS
    backoff = RETRY_BACKOFF_BASE
    attempt = 0
    while True:
        attempt += 1
        try:
            return client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_search=types.GoogleSearch())]
                ),
            ).text
        except Exception as e:
            remaining = deadline - time.monotonic()
            if _is_transient(e) and remaining > 0:
                delay = min(_retry_delay(e, backoff), remaining)
                print(f"  Transient error (attempt {attempt}): {e}. Retrying in {delay:.0f}s...")
                time.sleep(delay)
                backoff = min(backoff * 2, 300)
            else:
                raise


def find_previous_report(topic_name: str, today_str: str) -> str | None:
    """Return the content of the most recent previous report for this topic, if any."""
    pattern = os.path.join(REPORTS_DIR, f"{topic_name}_*.md")
    candidates = sorted(
        (p for p in glob.glob(pattern) if today_str not in os.path.basename(p)),
        reverse=True,
    )
    if not candidates:
        return None
    with open(candidates[0], "r", encoding="utf-8") as f:
        return f.read()


def research_topic(topic_content: str) -> str:
    """Ask Gemini to research the topic using its built-in Google Search grounding."""
    prompt = (
        "You are an expert research analyst. Research the following topic using current "
        "web sources and write a comprehensive Markdown report.\n\n"
        "IMPORTANT: Only include URLs that were actually returned by your search tool. "
        "Do not invent, guess, or construct any URLs. If you are not certain a URL exists "
        "and was retrieved by search, omit it entirely.\n\n"
        "Format the report with:\n"
        "- Clear headings and bullet points\n"
        "- A brief executive summary at the top\n"
        "- A ## Sources section at the end listing only real, searched URLs\n\n"
        f"## Topic\n\n{topic_content}"
    )
    return _gemini_with_search(prompt)


HTTP_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AutoReport link-checker)"}


def _check_url(url: str) -> bool:
    """Return True if the URL resolves successfully."""
    url = url.rstrip(".,;:")
    try:
        resp = requests.head(url, headers=HTTP_HEADERS, timeout=10, allow_redirects=True)
        if resp.status_code >= 400:
            resp = requests.get(url, headers=HTTP_HEADERS, timeout=10, stream=True)
        return resp.status_code < 400
    except Exception:
        return False


def _extract_urls(text: str) -> set[str]:
    return {u.rstrip(".,;:") for u in re.findall(r'https?://[^\s\)\]\"\']+', text)}


def fix_and_validate_links(text: str) -> str:
    """Validate every URL in the report. For dead links, ask Gemini to find a working
    replacement via search. If no replacement is found, rewrite the surrounding text to
    remove unverifiable claims. Finally convert all links to open in new tabs."""

    urls = _extract_urls(text)
    if not urls:
        return linkify_new_tabs(text)

    dead = set()
    for url in urls:
        # Before any string operations on links, add a null check
        if url is None or not isinstance(url, str):
            print(f"Warning: Invalid link encountered, skipping: {url}")
            continue
        
        if _check_url(url):
            print(f"  [ok] {url}")
        else:
            dead.add(url)
            print(f"  [dead] {url}")

    if dead:
        print(f"  Asking Gemini to replace or rewrite {len(dead)} dead link(s)...")
        dead_list = "\n".join(f"- {u}" for u in sorted(dead))
        prompt = (
            "You are editing a research report. Some URLs in the report are broken and must be fixed.\n\n"
            "For each dead URL below, either:\n"
            "  (a) Find a real, working replacement URL via search that supports the same claim, "
            "and substitute it in the report, OR\n"
            "  (b) If no valid source can be found, rewrite the sentence or bullet point that "
            "referenced that URL so it no longer makes that specific unverifiable claim.\n\n"
            "Return the complete corrected report text and nothing else. "
            "Do not add any preamble or explanation outside the report.\n\n"
            f"Dead URLs:\n{dead_list}\n\n"
            f"Report:\n{text}"
        )
        text = _gemini_with_search(prompt)

        # Verify the replacements Gemini introduced are also real
        new_urls = _extract_urls(text) - (urls - dead)
        still_dead = set()
        for u in new_urls:
            # Before any string operations on links, add a null check
            if u is None or not isinstance(u, str):
                print(f"Warning: Invalid link encountered in replacement, skipping: {u}")
                continue
            if not _check_url(u):
                still_dead.add(u)
        
        for url in still_dead:
            print(f"  [replacement also dead, stripping] {url}")
            text = re.sub(
                r'\[([^\]]+)\]\(' + re.escape(url) + r'\)',
                r'\1',
                text,
            )
            text = text.replace(url, "")

    return linkify_new_tabs(text)


def linkify_new_tabs(text: str) -> str:
    """Convert markdown links to HTML anchors that open in a new tab."""
    return re.sub(
        r'\[([^\]]+)\]\((https?://[^\)]+)\)',
        r'<a href="\2" target="_blank">\1</a>',
        text,
    )


def summarize_changes(display_name: str, previous_report: str | None, new_report: str) -> str:
    """Ask Gemini to produce a 2-3 sentence summary of what changed since the last report."""
    if previous_report:
        prompt = (
            f"You are summarizing changes in a weekly research report on '{display_name}'.\n\n"
            "Compare the previous report and the new report below. "
            "In 2-3 sentences, highlight only the most significant new developments, "
            "changes, or trends since the previous report. Be specific and concise.\n\n"
            f"## Previous Report\n\n{previous_report}\n\n"
            f"## New Report\n\n{new_report}"
        )
    else:
        prompt = (
            f"You are summarizing a research report on '{display_name}'.\n\n"
            "In 2-3 sentences, highlight the most important findings from this report. "
            "Be specific and concise.\n\n"
            f"## Report\n\n{new_report}"
        )
    return _gemini(prompt).strip()


def update_readme(new_log_block: str) -> None:
    """Replace the content between the README log markers with new_log_block."""
    if not os.path.exists(README_FILE):
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(
                "# AutoReport\n\nAutomated weekly research reports.\n\n"
                f"## Recent Activity\n\n"
                f"{README_MARKER_START}\n{README_MARKER_END}\n"
            )

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if README_MARKER_START in content and README_MARKER_END in content:
        before = content.split(README_MARKER_START)[0]
        after = content.split(README_MARKER_END)[1]
        new_content = (
            before
            + README_MARKER_START + "\n"
            + new_log_block
            + README_MARKER_END
            + after
        )
    else:
        new_content = (
            content.rstrip()
            + "\n\n## Recent Activity\n\n"
            + README_MARKER_START + "\n"
            + new_log_block
            + README_MARKER_END + "\n"
        )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)


# --- Main ---

def main() -> None:
    today_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    topic_files = sorted(glob.glob(os.path.join(TOPICS_DIR, "*.md")))

    if not topic_files:
        print(f"No .md files found in '{TOPICS_DIR}'. Nothing to do.")
        return

    succeeded = 0
    failed = 0
    topic_summaries = []  # list of (display_name, report_filename | None, summary | error_msg)

    for file_path in topic_files:
        filename = os.path.basename(file_path)
        topic_name = os.path.splitext(filename)[0]
        report_filename = f"{topic_name}_{today_str}.md"
        report_path = os.path.join(REPORTS_DIR, report_filename)
        display_name = topic_name.replace("_", " ").title()

        print(f"\nProcessing: {topic_name}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                topic_content = f.read()

            previous_report = find_previous_report(topic_name, today_str)
            if previous_report:
                print("  Found previous report — will summarize changes.")
            else:
                print("  No previous report — will summarize key findings.")

            print("  Researching and synthesizing report...")
            report_body = research_topic(topic_content)

            print("  Validating and fixing links...")
            report_body = fix_and_validate_links(report_body)

            with open(report_path, "w", encoding="utf-8") as f:
                f.write(f"# Research Report: {display_name}\n")
                f.write(f"*Generated: {today_str} UTC*\n\n")
                f.write(report_body)

            print(f"  Saved: {report_path}")

            print("  Generating README summary...")
            summary = summarize_changes(display_name, previous_report, report_body)

            succeeded += 1
            topic_summaries.append((display_name, filename, report_filename, summary))

        except Exception as e:
            print(f"  ERROR: {e}")
            topic_summaries.append((display_name, filename, None, f"Generation failed: {e}"))
            failed += 1

    # Build README log block
    total = succeeded + failed
    status_line = f"**{succeeded}/{total} reports generated successfully.**"
    if failed:
        status_line += f" {failed} failed — see workflow logs for details."

    log_parts = [f"### Run: {today_str}\n", status_line + "\n"]

    for display_name, topic_filename, report_filename, summary in topic_summaries:
        topic_link = f"[{topic_filename}]({TOPICS_DIR}/{topic_filename})"
        if report_filename:
            report_link = f"[{report_filename}]({REPORTS_DIR}/{report_filename})"
            log_parts.append(f"\n#### {display_name} — {topic_link} | {report_link}\n")
        else:
            log_parts.append(f"\n#### {display_name} — {topic_link} | generation failed\n")
        log_parts.append(f"{summary}\n")

    log_block = "\n".join(log_parts) + "\n"
    print("\nUpdating README.md...")
    update_readme(log_block)

    if failed:
        raise SystemExit("One or more topics failed. See output above.")


if __name__ == "__main__":
    main()
