# _sources — raw material

Raw data that feeds every AI role of the cockpit. Skills read these files directly from disk when they need raw material (numbers, decisions, market intelligence).

## Structure

```
_sources/
├── transcriptions/
│   ├── internal/            # Internal meetings (strategy, syncs, board)
│   └── clients/             # Client meetings, one folder per client
│       └── <client-name>/
├── reports/                 # Raw data (internal studies, benchmarks, industry reports)
└── research/                # Market intelligence — external articles, notes, observations
```

## What each subfolder is for

### `transcriptions/` — meeting minutes

- **Format**: Markdown, ideally Gemini Notes format (H3 sections: Summary / Résumé, Next steps / Étapes suivantes, Details / Détails with timestamps). The parser handles both English and French heading variants.
- **Fed by**: manual drop after each important meeting.
- **Naming convention**: `YYYY-MM-DD-subject.md`.
- **Value**: contains decisions and action items usable as source of truth by content agents ("what did we decide about X at the last sync?").

### `reports/` — quantitative data

- **Format**: Markdown, ideally structured with H2 sections.
- **Fed by**: manual drop when a new study / benchmark / internal research is complete.
- **Naming convention**: `YYYY-MM-DD-type-subject.md`.
- **Value**: canonical source for every number cited in published content. Agents must verify each number against this folder (grep / direct file reads).

### `research/` — market intelligence

Landing pad for all external market intelligence: competitor observations, industry trends, regulation updates, AI progress, news. Keeps the cockpit current without relying on stale training data.

**Automation candidates** (not shipped):
- RSS feeds (industry blogs, analyst firms, competitor newsrooms)
- Third-party newsletters parsed via a Gmail integration + Gemini auto-summary
- Google Alerts / Talkwalker turned into markdown
- Web agents monitoring key pages (competitor pricing, release notes, job boards)
- Competitor analysis screenshots via Gemini vision OCR

**Extension suggestion**: add Python scripts in `_integrations/research/` (or an n8n workflow, module `veille`) that drop markdown files matching the convention below.

**Recommended file shape** for research items (manual or automated):

```markdown
---
source: "Gartner Report 2026"
url: "https://www.gartner.com/..."
author: "Gartner Research"
date: 2026-04-15
tags: [industry, trends, ai]
---

# Title of the article

## Summary (1-2 sentences)
...

## Key points
- ...
- ...

## Relevance to our company
...

## Quotable excerpt
"..." (page/section)
```

## Privacy

- Files under these subfolders are **gitignored** by default (see `.gitignore`).
- Only this `README.md` and `.gitkeep` files are tracked.
- Raw meeting transcripts, internal reports, and research notes stay on your local machine. Nothing here is sent to any external service.
