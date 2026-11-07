---
name: wiki-lint
description: Health check for an llm-context-base wiki that ends in fixes the agent can make. Use when the user says "lint the wiki", "health check", "what's stale?", "what needs cleanup?", "what's orphaned?", "audit the wiki", or "are we being efficient with context?".
---

# Wiki health check

The point of a health check is fixes, not a report. Find what's wrong, then offer to fix the parts that matter most.

## Before you start

Read `.agents/wiki/config.md`. Its **Lint** section adapts the checks below to this folder: skip the checks it turns off, use its thresholds, and run the house-specific checks it adds. Its **House rules** section says what a fix must respect (link format, who writes frontmatter, where new pages may go).

Scan the folders in the Structure table plus any other folder holding notes; skip `.agents/`, `.claude/`, `.obsidian/`, `.git/` and the `private` folders. Change nothing without approval, except format-only link fixes when the user said "fix it".

## Checks

1. **Stale inbox.** Items in the inbox older than 7 days, by filename date or `updated`.
2. **Missing metadata.** Only when config `frontmatter` is `llm-context-base`: notes missing `type`, `summary` or `updated`, skipping `README.md` files. Frontmatter is added as notes are touched, so report this as a count per folder unless the user asked for a backfill.
3. **Stale and stuck notes.** `status: active` with `updated` more than 90 days ago (`archived`, `superseded`, `complete` exempt); drafts untouched for more than 30 days, including placeholder pages ("under construction", "TODO", empty bodies); `archived` or `superseded` without `failure_reason`. If a sync rewrites `updated`, judge age from other evidence (dates in titles, git history) and say so.
4. **Orphans.** Notes no other note links to, counting both `[[Note]]` and `[text](path.md)` links, links in the `related` field, and parent-child relationships the house rules define.
5. **Broken links and raw paths.** Links whose target doesn't exist; paths written as text or code spans where a link was meant; links the house's publisher would refuse.
6. **Naming.** Only when config `naming` is `date-prefixed`: notes without a `YYYY-MM-DD-` prefix (skip `README.md`, `AGENTS.md`, `CLAUDE.md`). Propose renames from the file's first commit date (`git log --diff-filter=A --follow --format=%ad --date=short -- <file> | tail -1`); renames update inbound links in the same pass.
7. **Context size.** `wc -l AGENTS.md .agents/wiki/config.md` and `wc -l .agents/skills/*/SKILL.md`. Flag `AGENTS.md` plus `config.md` over 300 lines, or a skill over 300 lines. For config, propose compacting Conventions: merge duplicates, drop rules the structure now makes obvious.
8. **House checks.** Whatever the Lint section of config adds.

## Report as fixes

Lead with what you propose to do, not with counts:

1. **The fixes worth doing, best first.** Up to five, each one line: what you'd change, where, and why it matters to the user (a page people land on is a placeholder; a decision's link points nowhere; ten meeting notes aren't reachable from their parent). Group mechanical fixes ("convert 23 code-span paths to links in Engineering/") into one line.
2. **One line of totals** for everything else, so nothing is hidden.
3. **An offer:** do the first fix now, or all the mechanical ones.

Keep the report short enough to read in one screen. If the user wants the full list, give it on request.

Monthly is a reasonable cadence, or whenever the wiki feels messy.
