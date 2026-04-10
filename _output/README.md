---
type: knowledge
summary: Generated artifacts that aren't part of the knowledge base - presentations, exports, reports, and other one-off outputs.
tags: [meta]
status: active
updated: 2026-04-09
---

# _output/

## Purpose

**Most of what you create belongs in the knowledge base - that's the point.** Knowledge compounds through use, and the wiki is where it lives.

This directory is for the exception: **throwaway artifacts** generated *from* your knowledge but not meant to live in it. Think of it as the difference between your notes (knowledge base) and the slide deck you exported for a specific meeting (output).

## What Goes Here

- Slide decks and presentations (Marp markdown, exported PDFs)
- Formatted reports and summaries
- Data exports and compilations
- One-off documents created for a specific audience or meeting
- Any generated artifact that doesn't need to be queried later

## What Does NOT Go Here

- Knowledge articles, how-tos, decision records → `2-Knowledge/`
- Meeting notes, journal entries → `3-Journal/`
- Work-in-progress initiatives → `1-Projects/`
- Raw captures → `_inbox/`

## File Naming

Date-prefixed for easy chronological browsing:
```
YYYY-MM-DD-[description].[ext]
```

Examples:
- `2026-04-07-q1-review-slides.md`
- `2026-04-07-team-summary-report.md`
- `2026-04-15-board-presentation.md`

## Git Behavior

**This directory is gitignored by default.** Most outputs are ephemeral - you generate them, use them, and move on.

If you want to version-control your outputs (e.g., you generate recurring reports and want history), remove the `_output/` line from `.gitignore`.

## Recommended Tools

- **[Marp](https://marp.app/)** - Generate slide decks from markdown. Write slides in `_output/`, render to PDF/HTML/PPTX. Your AI can create Marp-formatted slides directly from your knowledge base. *(Recommended by [Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))*
