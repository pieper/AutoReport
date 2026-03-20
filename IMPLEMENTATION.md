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

## Adding Topics

1. Create a new `.md` file in `topics/` — for example `topics/my_topic.md`
2. Describe what you want researched and any preferences for report format
3. Commit and push — the topic will be picked up on the next run
