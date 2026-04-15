# Marketing Copilot Template

> 🇫🇷 [Lire en français](README.fr.md)

> An opinionated, role-based AI marketing copilot for Claude Code with semantic memory, brand-enforcement hooks, and tool-agnostic integrations. Bootstrap in 30 minutes for any company.

**Recommended model**: Claude Opus 4.6. The system is designed to take advantage of Opus' long-context reasoning and strategic planning. Smaller models will work but with noticeable degradation on content-strategy, brand-check, and copy-editing tasks.

---

## What this is

A complete, opinionated scaffolding to turn Claude Code into a full-stack marketing copilot for your company. It assumes:

- You have a brand (voice, values, personas, proof points) worth enforcing consistently
- You publish content across multiple channels (LinkedIn, newsletters, blog, events, web)
- You want AI agents that learn from your past content, not invent from scratch every time
- You want deterministic brand compliance, not "I'll try to remember the rules"

The template ships with:

- **9 role folders** organized like a marketing team: `01-brand/`, `02-strategy/`, `03-social-media/`, `04-email/`, `05-web-content/`, `06-graphic-design/`, `07-events/`, `08-mail-signatures/`, `09-blog-seo/`. Each folder has a `CLAUDE.md` that teaches Claude Code how to operate in that role.
- **9 skills** (in `.agents/skills/`) that encode marketing best practices adapted to your brand: `brand-check`, `social-content`, `email`, `copywriting`, `copy-editing`, `content-strategy`, `seo`, `event-marketing`, and `image-generation` (brand-compliant visuals via Gemini nano-banana-pro).
- **Qdrant-based semantic memory** (`_integrations/qdrant/`) that ingests everything you publish and everything in your brand doctrine, so every agent can ask "has this been said before?" and "what does the doctrine say about X?" in 500ms.
- **Brand-compliant AI image generation** via Gemini `gemini-3-pro-image-preview` (nano-banana-pro). Every prompt is automatically prefixed with your color palette, typography, illustration style, and banned visual tropes, so every generated image respects the brand without manual prompting.
- **A brand-check hook** that fires automatically after any content write and blocks delivery if the draft violates brand standards.
- **A weekly multi-source sync** (macOS launchd) that keeps the memory up to date without you thinking about it.
- **A bootstrap interview** that onboards your company in about 30 minutes, starting from your website URL and any brand docs you already have.

## Philosophy

Three principles drive every design decision:

1. **Brand as truth** — `01-brand/` is the source of truth. Every other role defers to it. Any contradiction is flagged before publication, not after.
2. **Retrieval-first** — Every creative act is preceded by a semantic search: "has this been said already?", "what's the canonical phrasing?", "what chiffres are backed by the doctrine?" No invention without verification.
3. **Hook-enforced** — The harness enforces the workflow, not Claude's willpower. A PostToolUse hook fires the brand check whenever content is written in a production folder. The system is deterministic, not hopeful.

## Who this is for

**Good fit**:
- SaaS companies with a clear brand voice and multiple content channels
- Agencies publishing for themselves (not for clients directly)
- Collectives and freelance groups that need consistency without a full-time editor
- Consultancies with proprietary data (benchmarks, reports, case studies) to surface in content
- Any team that publishes 5+ pieces of content per week across 2+ channels

**Poor fit**:
- Mass-market B2C with no strong doctrine (every piece is a one-off)
- Single-channel publishers (just LinkedIn, just blog) who don't need cross-channel coordination
- Teams that don't have brand guidelines yet (build them first, then come back)

## Architecture at a glance

```
your-company-copilot/
├── CLAUDE.md                         # Orchestrator + bootstrap detector
├── 01-brand/                         # Source of truth (editorial charter, personas, messaging)
├── 02-strategy/                      # Editorial planning, pillars, KPIs
├── 03-social-media/                  # LinkedIn, Discord, WhatsApp
├── 04-email/                         # Newsletters, promos, sales outreach, nurturing
├── 05-web-content/                   # Landing pages, HTML artifacts
├── 06-graphic-design/                # Visual creation, briefs, AI image prompts
├── 07-events/                        # Event communication plans
├── 08-mail-signatures/               # HTML signatures per member
├── 09-blog-seo/                      # Long-form SEO content
├── .agents/skills/                   # 8 role-specific skills
├── .claude/hooks/                    # brand-check-reminder.py
├── _integrations/qdrant/             # Semantic memory pipeline
│   ├── sync.py                       # CLI (sync, query, verify, stats)
│   ├── mcp_server.py                 # MCP server wrapping Gemini + Qdrant
│   ├── config.yaml                   # Sources, enrichers, functionalities mapping
│   ├── runbook.md                    # Full workflow documentation
│   └── cron/                         # Weekly launchd job with drift detection
├── _sources/                         # Raw inputs (transcripts, reports, veille/research)
└── _bootstrap/                       # Interview protocol and templates (run once at setup)
```

## Quickstart

### 1. Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- macOS (for the launchd cron — Linux/WSL users can adapt to systemd or cron)
- Python 3.11+
- A [Qdrant Cloud](https://cloud.qdrant.io) account (free tier works, 1 GB)
- A [Google AI Studio](https://aistudio.google.com/apikey) API key for Gemini embeddings

### 2. Clone and install

```bash
git clone https://github.com/YOUR_USERNAME/marketing-copilot-template.git your-company-copilot
cd your-company-copilot

pip install qdrant-client google-genai python-dotenv pyyaml requests mcp
```

### 3. Open in Claude Code

```bash
claude .
```

Claude will detect that `.setup-completed` does not exist and will automatically start the bootstrap interview (see `_bootstrap/interview.md`). The interview walks you through:

- **Phase 0 — Discovery**: Claude analyzes your website and any brand documents you drop into `_bootstrap/inputs/` (vision, mission, brand guide, pitch deck, existing content samples)
- **Phase 1 — Identity validation**: Claude presents what it understood and you correct anything wrong
- **Phase 2 — Personas**: 2-4 personas built collaboratively with your help
- **Phase 3 — Functionalities**: you pick which functionalities you want (editorial calendar, email marketing, knowledge base, events, CRM) and which tool backs each one. The system is tool-agnostic — you can plug Notion, Airtable, MailerLite, Mailchimp, Outline, Confluence, or a custom connector.
- **Phase 4 — Skills personalization**: tweak the 8 skills to match your voice

At the end of the interview, Claude:
- Writes your answers into the appropriate CLAUDE.md files and skills
- Initializes the Qdrant collection (if you enabled it)
- Runs an initial ingestion of your brand documents
- Creates the `.setup-completed` marker

Expected duration: 20-40 minutes depending on how much existing material you have.

### 4. Start operating

Open Claude Code and ask for anything:

```
> Rédige un post LinkedIn sur [topic]
> Prépare la newsletter de [month]
> Crée une landing page pour [product]
> Plan de com complet pour [event]
> Que dit notre doctrine sur [subject] ?
```

Each request triggers the relevant role, which consults Qdrant for past content and brand doctrine, drafts the piece, runs the brand-check, and delivers.

## Features in detail

### Semantic memory (Qdrant + Gemini)

Every piece of content you publish, every meeting transcript, every page of your brand doctrine, and every article in your knowledge base gets indexed with Google's `gemini-embedding-001` (3072 native dimensions) and stored in Qdrant. At retrieval time, the MCP server exposes 3 tools to Claude:

- `qdrant_search(query, top, filters)` — semantic retrieval with optional filters (type, source, channel)
- `qdrant_find_similar(text, threshold, exclude_source_file)` — anti-repetition check before publishing
- `qdrant_stats()` — collection stats and registry health

Each document is enriched at ingestion time with:
- A 2-sentence summary (Gemini 2.5 Flash)
- Flat entity list (clients, people, tools, figures, locations)
- 3-5 factual claims
- Content hash (SHA-256) for deduplication
- For meetings: decisions and action items extracted from the transcript

### Brand-check hook

Whenever Claude writes or edits a Markdown or HTML file in `03-social-media/`, `04-email/`, `05-web-content/`, `07-events/`, or `09-blog-seo/`, a `PostToolUse` hook injects a system reminder that forces Claude to invoke the `brand-check` skill before delivering. The skill applies a 5-point filter (vocabulary, tone, proof, audience, visual) and a Qdrant-powered anti-repetition check. Verdicts: ✅ PASS / 🟠 FIX / 🔴 BLOCK. No draft ships without passing.

### Incremental sync

`sync.py` is idempotent. Running it twice in a row does nothing the second time because a local `registry.json` tracks content hashes and deleted point IDs. On content change, it surgically removes the old chunks before re-inserting. No drift between Qdrant and the local source of truth.

Weekly automation via macOS launchd (`cron/run-weekly-sync.sh`) covers all sources. A `--verify` drift check runs after each sync; a macOS notification fires if drift is detected.

### Brand-compliant image generation

The `image-generation` skill wraps Google's `gemini-3-pro-image-preview` (a.k.a. nano-banana-pro) with your brand guidelines automatically injected. You describe what you need in plain language — "a hero image for our landing page about SEO" — and the skill:

1. Reads `01-brand/style-guide.md` to pull your color palette, typography, illustration style, and banned visual tropes (stock photos, generic office imagery, etc.)
2. Prefixes your prompt with these constraints in a structured way that Gemini respects
3. Generates the image and saves it to `06-graphic-design/outputs/` with a metadata sidecar noting the prompt used
4. Flags visible breaches of your style guide for review

This uses the same `GOOGLE_AI_API_KEY` as the embeddings and enrichment — one key, three capabilities. Activation is automatic if the key is present.

### Tool-agnostic functionalities

The `config.yaml` describes your stack by functionality, not by tool:

```yaml
functionalities:
  editorial_calendar:
    tool: notion              # or airtable, trello, google-sheets, custom, none
    enabled: true
  email_marketing:
    tool: mailerlite          # or mailchimp, convertkit, brevo, resend, custom, none
    enabled: true
  knowledge_base:
    tool: outline             # or notion, confluence, gitbook, custom, none
    enabled: false
```

Swapping a tool means changing one line. Built-in connectors cover the most common tools; for anything else, a "custom" stub is generated with clear TODO comments so you can implement your own connector in under an hour.

## Is Qdrant mandatory?

**Technically no, practically yes.** The system works without Qdrant — the skills fall back to reading files directly — but you lose ~80% of the value:

- No anti-repetition check (agents will happily write the same LinkedIn post twice)
- No cross-channel consistency (a claim in a blog post may contradict last month's newsletter)
- No fast retrieval from your brand doctrine (each agent has to re-read `01-brand/` every session)
- No meeting-to-content surfacing (transcripts stay invisible)

You can run the bootstrap without Qdrant, operate for a few weeks to see if the rest of the system fits, then enable Qdrant later via `_integrations/qdrant/init_collection.py`. Enabling it takes about 5 minutes once you have a cluster URL and API key.

## Contributing

PRs welcome. This template is meant to evolve. Areas of interest:
- New source connectors (Airtable, Confluence, GitBook, ClickUp, ...)
- New enrichers (sentiment, tonality match, pillar classifier)
- Linux/WSL cron equivalents (systemd timers)
- More skills (PR newsletter, case study builder, report ghostwriter)
- Translations of the bootstrap interview to other languages

See [CONTRIBUTING.md](CONTRIBUTING.md) (if present) for guidelines.

## Credits

Inspired by the real-world setup of a digital transformation consulting collective that needed a marketing copilot to keep 100+ members and 8 brand channels aligned. The original implementation is private; this template is the distilled, anonymized, publishable version.

## License

MIT. See [LICENSE](LICENSE).
