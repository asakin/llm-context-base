---
name: wiki-lint
description: Health check for an llm-context-base wiki. Use when the user says "lint the wiki", "health check", "what's stale?", "what needs cleanup?", "what's orphaned?", "audit the wiki", or "are we being efficient with context?".
---

# Wiki health check

Read `.agents/wiki/config.md` first. Scan the folders in its Structure table plus any other folder holding notes; skip `.agents/`, `.claude/`, `.obsidian/`, `.git/` and the `private` folders (count their files, don't read them). Lint reports and proposes. Change nothing without approval, except format-only link fixes in check 5 when the user said "fix it".

Run the checks in order and report only the ones with findings.

## 1. Stale inbox

Files in the inbox older than 7 days, by filename date or `updated`.

```text
STALE INBOX (2, older than 7 days)
- inbox/2026-03-28-vendor-note.md: 10 days
→ file, update or discard
```

## 2. Missing metadata

Notes without YAML frontmatter or missing `type`, `summary` or `updated`. Skip `README.md` files. In a folder adopted from an existing vault, report the count per folder rather than every file; frontmatter is added when a note is next touched, not in bulk, unless the user asks for a backfill.

## 3. Stale and stuck notes

- `status: active` with `updated` more than 90 days ago. `archived`, `superseded` and `complete` notes are exempt.
- `status: draft` with `updated` more than 30 days ago: propose finishing, filing or archiving it.
- `archived` or `superseded` without `failure_reason`.

## 4. Orphans

Notes no other note links to. Count both link styles: `[[Note name]]` (also `[[path/Note name|alias]]`) and `[text](path.md)`, including links inside the `related` frontmatter field. Propose a note to link from, or archiving.

## 5. Broken links and raw paths

- Links whose target doesn't exist: list them for manual resolution.
- Paths written as text or code spans (`` `Knowledge/foo.md` ``) where a link was meant: propose converting them to the configured link style (`wikilink` → strip `.md`, wrap in `[[ ]]`).

## 6. Naming

Only when config `naming` is `date-prefixed`: notes outside the exceptions (`README.md`, `AGENTS.md`, `CLAUDE.md`, the log) without a `YYYY-MM-DD-` prefix. Propose renames using the file's first commit date (`git log --diff-filter=A --follow --format=%ad --date=short -- <file> | tail -1`), or today's date if untracked. Renames must update inbound links in the same pass. For `descriptive` or `as-found`, skip this check.

## 7. Context size

What the agent loads every session should stay small as the wiki grows.

```bash
wc -l AGENTS.md CLAUDE.md .agents/wiki/config.md
wc -l .agents/skills/*/SKILL.md | sort -rn
```

Flag `AGENTS.md` plus `config.md` over 300 lines, any skill over 300 lines, any template over 100 lines. For config, propose compacting the Conventions section: merge duplicates, drop rules that are now obvious from the structure. Never restructure instruction files without approval, and don't optimize what isn't a problem.

## Report

```text
WIKI LINT, YYYY-MM-DD: 7 checks, 5 findings
[sections with findings]
```

Append to the log: `## [YYYY-MM-DD] lint | 5 findings: stale 2, metadata 1, orphans 2`.

Monthly is a reasonable cadence, or whenever the wiki feels messy.
