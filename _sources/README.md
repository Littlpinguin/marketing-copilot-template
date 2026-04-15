# _sources — Raw material

This folder contains the raw data that feeds all the AI roles of the copilot. Everything here is indexed in Qdrant (collection configured in `_integrations/qdrant/config.yaml`) for fast semantic retrieval.

## Structure

```
_sources/
├── transcriptions/
│   ├── internal/            # Internal meetings (strategy, syncs, board)
│   └── clients/             # Client meetings, organized per client
│       └── <client-name>/
├── reports/                 # Raw data (internal studies, benchmarks, industry reports)
└── research/                # Market intelligence (veille) — external articles, notes, observations
```

## Role of each subfolder

### `transcriptions/` — meeting minutes

- **Format**: markdown, ideally the Gemini Notes format (Résumé / Étapes suivantes / Détails with timestamps)
- **Fed by**: manual drop after each important meeting
- **Naming convention**: `YYYY-MM-DD-subject.md`
- **Special chunking**: structural sections stay as their own chunks, Détails bullets are grouped by token budget (see `_integrations/qdrant/utils.py::chunk_by_transcript_section`)
- **Value**: contains decisions and action items usable as source of truth by content agents ("what did we decide about X at the last sync?")

### `reports/` — quantitative data

- **Format**: markdown, ideally structured with H2 sections
- **Fed by**: manual drop when a new study / benchmark / internal research is complete
- **Naming convention**: `YYYY-MM-DD-type-subject.md`
- **Value**: canonical source for every chiffre cited in published content. Agents must verify each number against this folder (via Qdrant `filter_source_key=reports`).

### `research/` — market intelligence (veille)

**Role**: This folder is the landing pad for all external market intelligence. Anything observed about the market, competitors, trends, regulations, AI progress, industry news — should end up here as markdown files for indexing and retrieval.

**Automation candidates** (not yet implemented):
- RSS feeds (industry blogs, Gartner, Forrester, competitor newsrooms)
- Third-party newsletters parsed via Gmail API + Gemini (auto-summary)
- Google Alerts / Talkwalker transformed into markdown
- Web agents monitoring key pages (competitor pricing, release notes, job boards)
- Competitor analysis screenshots with Gemini vision OCR

**TODO (next iteration)**: automate the feeding of `research/`. The suggested architecture is one or several Python scripts in `_integrations/veille/` that drop markdown files conforming to the naming convention below, then a cron triggers `sync.py --source research` after each drop.

**Recommended file format for research items** (manual or automated):

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

## Metadata extracted automatically during ingestion

- `source_type`: transcription | report | research-note
- `client`: name of the client (if in `transcriptions/clients/`)
- `date`: extracted from filename or frontmatter
- `tags`: from frontmatter or detected in content
- `participants`: for transcriptions, extracted from the header
- `entities`: extracted by the `entities` enricher (clients, people, tools, numbers)
- `summary`: 2-sentence auto-summary
- `claims`: 3-5 factual claims
- `decisions` and `action_items`: for transcripts only, extracted by the `meeting` enricher

## Manual ingestion

```bash
cd _integrations/qdrant
python3 sync.py --source transcripts
python3 sync.py --source reports
python3 sync.py --source research
# or all at once
python3 sync.py --all
```

## Privacy note

- Files in these subfolders are **git-ignored** by default (see `.gitignore`)
- Only this `README.md` and `.gitkeep` files are tracked
- Your raw meeting transcripts, internal reports, and research notes stay on your local machine. The Qdrant cloud holds the embeddings (numerical) and the chunked text payload. Be aware that if you use Qdrant Cloud, the chunked text is stored in Qdrant's infrastructure. For sensitive content, consider running Qdrant self-hosted instead (a flag is available in `_integrations/qdrant/config.yaml`).
