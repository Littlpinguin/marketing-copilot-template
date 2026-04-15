# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-04-15

### Added
- Initial template release
- 9 role folders (brand, strategy, social media, email, web content, graphic design, events, mail signatures, blog & SEO) each with its CLAUDE.md template
- 8 generic marketing skills (brand-check, social-content, email, copywriting, copy-editing, content-strategy, seo, event-marketing)
- Qdrant semantic memory pipeline (sync.py, utils.py, init_collection.py, mcp_server.py) with Gemini embedding-001 (3072 dim)
- 4 source connectors: filesystem, notion, outline, transcripts
- 5 enrichers: hash, summary, entities, claims, meeting
- Brand check hook (PostToolUse) that forces brand validation before content delivery
- Weekly multi-source cron with drift detection (macOS launchd)
- Bootstrap interview in 5 phases (discovery, identity, personas, functionalities, skills) with website auto-analysis
- Tools-agnostic design: functionalities first, tools second (Notion / Airtable / MailerLite / Mailchimp / Outline / Confluence / etc.)
- MIT License
