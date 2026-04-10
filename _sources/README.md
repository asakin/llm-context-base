---
type: knowledge
summary: Optional archive of preserved source documents - originals kept when the AI judges them important enough to retain.
tags: [meta]
status: active
updated: 2026-04-09
---

# _sources/

## Purpose

When you ingest a source (an article, a PDF, a clipped web page), the knowledge gets extracted into your wiki and the original in `_inbox/` gets discarded after 7 days. That's the default - most originals aren't worth keeping.

But sometimes a source is important enough to preserve:
- A key architecture document you may want to re-process later
- A research paper you'll reference repeatedly
- An article whose URL might disappear
- Anything you'd want to re-ingest when a smarter model becomes available

**This directory is opt-in.** Set `Preserve Important Sources: yes` in `_config/config.md` to enable it. When enabled, your AI will use its judgment to decide which sources are worth keeping here. During training, it will calibrate with you - asking once or twice whether you want a particular source preserved, then learning your preferences.

## How It Works

1. A capture arrives in `_inbox/`
2. The AI files the knowledge into the wiki (as usual)
3. If the source is judged important AND preservation is enabled, the original is moved to `_sources/` instead of being discarded
4. Sources here are **immutable** - they're reference copies, not working documents

## File Naming

```
YYYY-MM-DD-[description].[ext]
```

Examples:
- `2026-04-07-kubernetes-architecture-whitepaper.md`
- `2026-04-10-vendor-security-assessment.pdf`

## Git Behavior

**This directory is committed to git** (not gitignored). Sources are permanent reference material - they should travel with your repo.
