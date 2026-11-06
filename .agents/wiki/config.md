---
setup: pending          # wiki-setup sets this to the date it ran
inbox: inbox/           # where new captures land
log: log.md             # the one log of significant wiki changes
link_style: wikilink    # wikilink | markdown
naming: descriptive     # descriptive | date-prefixed | as-found (keep whatever each folder already does)
private: []             # folders agents must not quote from or write to without asking, e.g. [Journal/, Private/]
preserve_sources: false # true: keep important originals in sources/ when filing
extra_frontmatter: []   # frontmatter fields this folder already uses, kept alongside the standard ones
---

# Wiki configuration

This file belongs to you. Your AI reads it before working in the wiki and adds to it as it learns how you work. llm-context-base updates never overwrite it.

## About you

<!-- wiki-setup fills this in from a few questions. Edit freely. -->

- **Name:**
- **Role:**
- **What this wiki is for:**
- **Context:** (domain, team, tools, key people)

## Tone

How the AI talks to you in chat. Files always use a plain, professional register.

- Conversational and direct, like a technically sharp colleague
- Short answers by default: lead with the answer or the action
- When you produce a file, don't summarize what you just wrote

## Structure

Where things go. wiki-setup writes what it finds in the folder; the AI adds folders as you approve them.

| Folder | What goes there |
|---|---|
| `inbox/` | New captures, filed within about a week |

## Conventions

Rules and preferences learned while working together, newest last. Format: `- YYYY-MM-DD: rule`.

## Tools

Local tools the AI may offer to install when a task needs them. Add entries in the same shape.

- **Marp** — markdown to slides and PDF. Install: `npm install -g @marp-team/marp-cli`. Use when asked for slides or a PDF. Status: not installed.
