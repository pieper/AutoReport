# AutoReport — Implementation Guide

## Repository Structure

```
AutoReport/
├── .github/
│   └── workflows/
│       └── weekly-report.yml   # GitHub Actions cron workflow
├── scripts/
│   └── generate_report.py      # Main report generation script
├── topics/                     # Input: one .md file per research topic
├── reports/                    # Output: generated reports (one per topic)
├── requirements.txt
├── .env.example                # Template for local API key configuration
└── README.md
```

---

## Getting API Keys

Only one credential is required. The script uses Gemini's built-in Google Search grounding, so there is no need for a separate Custom Search API key or Programmable Search Engine.

### Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **Create API key**
3. Copy the key — you will use it as `GEMINI_API_KEY`

The free tier is sufficient for weekly runs across a moderate number of topics.

---

## Running Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Copy `.env.example` to `.env` and fill in your key:

```bash
cp .env.example .env
# edit .env with your actual key
```

The `.env` file is gitignored and will never be committed.

### 3. Add or edit a topic

Create a markdown file in `topics/`. The filename (without `.md`) becomes the report title. Describe what you want researched and any preferences for report format.

### 4. Run the script

```bash
python scripts/generate_report.py
```

Reports are written to `reports/` with a date stamp (e.g. `AI_topic_2026-03-17.md`) and `README.md` is updated with a run summary.

---

## Configuring GitHub Actions

### Add secrets to your repository

Navigate to **Settings > Secrets and variables > Actions** and add one repository secret:

| Secret name | Value |
| :--- | :--- |
| `GEMINI_API_KEY` | Your Gemini API key |

### Schedule

The workflow runs at **08:00 UTC every Monday**. To change the schedule, edit the `cron` expression in [.github/workflows/weekly-report.yml](.github/workflows/weekly-report.yml).

### Manual trigger

You can trigger a run at any time from the **Actions** tab in your repository. Click **Weekly Research Report > Run workflow**. An optional `topic_filter` input lets you process a single topic file by name for testing.

---

## Email Notifications via Google Apps Script

The workflow itself does not send email. Instead, a small Google Apps Script runs on its own weekly schedule, fetches the README from GitHub, and emails you the summary using your Gmail account — no SMTP credentials or workflow changes needed.

### Setup

1. Go to [script.google.com](https://script.google.com) and create a new project
2. Paste the script below, filling in your repo details
3. For a **private repository**, also add a GitHub token:
   - **Project Settings > Script Properties > Add property**
   - Name: `GITHUB_TOKEN`, Value: a personal access token with `repo` read scope
4. Click **Run** once to trigger the OAuth consent prompt and verify it works
5. Add a weekly trigger: **Triggers (clock icon) > Add Trigger**
   - Function: `sendWeeklyReport`
   - Event source: Time-driven
   - Type: Week timer
   - Day: Monday, time: 9am–10am (or an hour after your cron job)

### Turning off email notifications

To stop the weekly email, go to your Apps Script project, click the **Triggers** icon (clock) in the left sidebar, find the `sendWeeklyReport` trigger, and delete it. To re-enable it, add the trigger again as described in the setup steps above.

### Script

```javascript
function sendWeeklyReport() {
  const OWNER  = "your-github-username";
  const REPO   = "AutoReport";
  const BRANCH = "main";
  const TO     = "your@email.com";

  const repoUrl   = `https://github.com/${OWNER}/${REPO}`;
  const scriptUrl = `https://script.google.com/home/projects/${ScriptApp.getScriptId()}`;
  const token = PropertiesService.getScriptProperties().getProperty("GITHUB_TOKEN");
  const rawUrl = `https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/README.md`;

  const options = token ? { headers: { Authorization: `token ${token}` } } : {};
  const content = UrlFetchApp.fetch(rawUrl, options).getContentText();

  const match = content.match(/<!-- REPORT_LOG_START -->([\s\S]*?)<!-- REPORT_LOG_END -->/);
  const summary = match ? match[1].trim() : "No summary found in README.";

  // Extract report file paths from heading lines like:
  // #### Topic Name — [topic.md](topics/topic.md) | [topic_2026-03-17.md](reports/topic_2026-03-17.md)
  const reportLinks = [];
  const headingPattern = /^#### (.+?) —.*\|\s*\[([^\]]+)\]\((reports\/[^\)]+)\)/gm;
  let m;
  while ((m = headingPattern.exec(summary)) !== null) {
    const label      = m[1].trim();
    const reportFile = m[2];
    const reportPath = m[3];
    reportLinks.push({ label, url: `${repoUrl}/blob/${BRANCH}/${reportPath}`, file: reportFile });
  }

  MailApp.sendEmail(TO, "AutoReport — Weekly Summary", summary, {
    htmlBody: markdownToHtml(summary) + buildFooterHtml(reportLinks, repoUrl, scriptUrl)
  });
}

function buildFooterHtml(reportLinks, repoUrl, scriptUrl) {
  const items = reportLinks
    .map(r => `<li><a href="${r.url}">${r.label} — ${r.file}</a></li>`)
    .join("\n");
  return `
    <hr>
    <p><strong>Reports</strong></p>
    <ul>${items}</ul>
    <p>
      <a href="${repoUrl}">View AutoReport repository</a> &nbsp;·&nbsp;
      <a href="${scriptUrl}">Edit this notification script</a>
    </p>`;
}

function markdownToHtml(md) {
  let html = md
    // Headings
    .replace(/^#### (.+)$/gm, "<h4>$1</h4>")
    .replace(/^### (.+)$/gm,  "<h3>$1</h3>")
    .replace(/^## (.+)$/gm,   "<h2>$1</h2>")
    .replace(/^# (.+)$/gm,    "<h1>$1</h1>")
    // Bold
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    // Markdown links
    .replace(/\[([^\]]+)\]\((https?:\/\/[^\)]+)\)/g, '<a href="$2">$1</a>')
    // Bullet points — collect runs into <ul> blocks
    .replace(/((?:^- .+\n?)+)/gm, (block) => {
      const items = block.trim().split("\n")
        .map(line => `<li>${line.replace(/^- /, "")}</li>`)
        .join("\n");
      return `<ul>${items}</ul>`;
    })
    // Horizontal rules
    .replace(/^---$/gm, "<hr>")
    // Blank lines between paragraphs
    .replace(/\n{2,}/g, "</p><p>")
    // Remaining single newlines
    .replace(/\n/g, "<br>");

  return `<div style="font-family:sans-serif;line-height:1.6;max-width:700px"><p>${html}</p></div>`;
}
```

---

## Adding Topics

1. Create a new `.md` file in `topics/` — for example `topics/my_topic.md`
2. Describe what you want researched and any preferences for report format
3. Commit and push — the topic will be picked up on the next run
