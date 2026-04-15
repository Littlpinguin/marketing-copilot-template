# Bootstrap inputs — Drop your existing material here

This folder is where you drop any existing brand or company material **before** answering the bootstrap interview. Claude Code will read everything here during Phase 0 (Discovery) and pre-fill as much as possible, so you don't have to retype information that already exists somewhere.

## What to drop here

Anything that describes your company, brand, voice, or strategy. Common examples:

- `brand-guide.pdf` (or `.md`, `.docx`)
- `editorial-charter.md`
- `pitch-deck.pdf` or `.pptx`
- `personas.md`
- `vision-mission.md`
- `positioning-statement.md`
- `messaging-framework.md`
- `writing-samples/` (a folder with 5-10 of your best past posts, emails, or articles)
- `website-dump.md` (if Claude can't fetch your website, paste your homepage text here)

## Accepted formats

- **Markdown (`.md`)** — ideal, read as-is
- **Plain text (`.txt`)** — read as-is
- **PDF** — Claude will try to extract text via `pdftotext` or similar
- **Word (`.docx`)** — Claude may ask you to export as PDF first
- **PowerPoint (`.pptx`)** — same
- **Screenshots (`.png`, `.jpg`)** — Claude will try to OCR / describe

## What Claude does with this content

1. Reads every file recursively during Phase 0 of the interview
2. Cross-references with what it extracted from your website (`WebFetch`)
3. Detects contradictions (e.g. website says "100+ clients", pitch deck says "50+")
4. Builds a draft company profile and asks you to validate/correct it section by section
5. Writes the validated profile into `01-brand/`

## Privacy and security

- This folder is **git-ignored** by default. Your raw material stays local and is never committed.
- After the bootstrap, the original files remain here for reference. You can delete them manually if you prefer.
- The bootstrap process writes into `01-brand/` which IS committed — review those files before pushing to a public repo.

## After the bootstrap

Once `.setup-completed` exists, this folder is no longer read automatically. You can still drop new material here manually and run the interview again with `cd _bootstrap && claude -p interview.md` to refresh the brand profile.
