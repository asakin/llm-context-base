---
setup: pending          # wiki-setup sets this to the date it ran
inbox: inbox/           # where new captures land; setup reuses an intake folder the folder already has
link_style: wikilink    # wikilink | markdown
naming: descriptive     # descriptive | date-prefixed | as-found (keep whatever each folder already does)
frontmatter: llm-context-base  # llm-context-base | host (another tool writes it; never touch) | none
private: []             # folders agents must not quote from or write to without asking, e.g. [Journal/, Private/]
preserve_sources: false # true: keep important originals when filing
sources: sources/       # where preserved originals go
---

# Wiki configuration

This file belongs to you. Your AI reads it before working in the wiki and adds to it as it learns how you work. llm-context-base updates never overwrite it; they re-adapt the skills from it. Where it disagrees with the llm-context-base block in `AGENTS.md`, this file wins.

## About you

<!-- wiki-setup fills this in from a few questions. Edit freely. -->

- **Name:**
- **Role:**
- **What this wiki is for:**
- **Context:** (domain, team, tools, key people)

## Tone

How the AI talks to you in chat. Files follow the folder's own style.

- Conversational and direct, like a technically sharp colleague
- Short answers by default: lead with the answer or the action
- When you produce a file, don't summarize what you just wrote

## House rules

How this folder worked before llm-context-base arrived, and how llm-context-base fits in. wiki-setup fills this in from the folder's instruction files, sync tooling, linters and existing notes. Each row says whether llm-context-base adopted the house rule, kept its own default, or changed something with your agreement.

| Topic | House rule | llm-context-base here |
|---|---|---|
| (none recorded yet) | | |

## Practices

How each llm-context-base practice (see `.agents/skills/wiki-setup/references/practices.md`) applies here: **in place** (the house already does it, and how), **adopted** (llm-context-base's default), **adapted** (how it was fitted to the house rules), or **declined** (and why).

| Practice | Here |
|---|---|
| (none recorded yet) | |

## Structure

Where things go. wiki-setup writes what it finds in the folder; the AI adds folders as you approve them.

| Folder | What goes there |
|---|---|
| `inbox/` | New captures, filed within about a week |

## Lint

How the `wiki-lint` checks are adapted to this folder: checks turned off and why, changed thresholds, and checks specific to this folder's house rules.

## Conventions

Rules and preferences learned while working together, newest last. Format: `- YYYY-MM-DD: rule`.

## Tools

Local tools the AI may offer to install when a task needs them. Add entries in the same shape.

- **Marp** — markdown to slides and PDF. Install: `npm install -g @marp-team/marp-cli`. Use when asked for slides or a PDF. Status: not installed.
