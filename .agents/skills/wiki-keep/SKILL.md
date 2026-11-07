---
name: wiki-keep
description: Keep an llm-context-base wiki in good order. Use when asked to maintain, tidy, restructure or garden the wiki, merge or split notes, fix links and metadata across many notes, archive or supersede notes, or improve prose and terminology without changing what notes claim.
---

# Keeping the wiki

The wiki is the durable artifact: keep it navigable, linked and faithful to what the user actually knows. Improve it; never replace the user's knowledge with your own. Read `.agents/wiki/config.md` first (house rules, practices, structure, paths, link style, frontmatter, private folders, conventions). The house rules outrank the defaults below. Templates for each note type are in `.agents/wiki/templates/`. For filing and capture follow `wiki-capture`; for health checks `wiki-lint`.

## What keeping covers

- **Filing:** extract durable claims, decisions, corrections and sources from the inbox; update existing notes before creating new ones.
- **Writing and updating** notes with correct metadata and links in the configured style.
- **Structure:** merge notes that are the same concept, split notes that have grown too broad, mark superseded notes with a trail to their replacement, convert raw paths to links, keep parent and index pages listing what they hold.
- **Language:** clarity, headings, summaries, consistent terminology. You decide how things are said, not what they claim.

## How to work

1. Start from a concrete goal: an inbox to file, a lint report, a note to write, a page to tidy.
2. For anything touching more than a handful of notes, first write a short map (notes affected, action, risk) and get approval.
3. Make the smallest coherent change, then update metadata and links.
4. Summarize what changed and what you left for the user to decide.

## Rules

- Never invent facts, sources, dates, decisions or preferences.
- Never delete content just because it looks old, and never archive an active note without leaving a link to what replaced it.
- Don't merge notes because they share keywords; merge only the same durable concept. Don't split unless each part has a clear purpose.
- Preserve citations, uncertainty, and corrections (the before and after). If a claim looks wrong or overconfident, flag it for the user, or for an investigation with `wiki-investigate`, instead of rewriting it.
- Don't mass-rename files without an approved plan; renames update inbound links in the same pass.
- Stay out of `private` folders unless the user asks.

A good pass leaves the wiki easier to browse and query, and more faithful to what the user knows.
