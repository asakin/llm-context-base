---
type: template
summary: Health-check pass for the wiki — surfaces stale metadata, missing standard blocks, orphaned files, and stale inbox items.
tags: [meta, maintenance]
status: active
updated: 2026-04-11
---

# Knowledge Lint

## Purpose

The lint pass is the wiki's health check. Run it when the system feels messy, when you want to know what's stale, or on a regular cadence (monthly recommended). It's the complement to knowledge capture — lint keeps existing knowledge fresh and consistent.

**Load this module when user says:**
- "lint the wiki" / "wiki health check" / "health check"
- "what's stale?" / "what needs cleanup?" / "what's orphaned?"
- "wiki cleanup" / "audit the system"

---

## Lint Checks (Run in Order)

### Check 1: Stale Inbox Items

**What:** Files in `_inbox/` older than 7 days.

**How:**
- List all files in `_inbox/` with their dates (from filename `YYYY-MM-DD-*` or `Updated:` field)
- Flag any older than 7 days

**Output format:**
```
📥 STALE INBOX (X items, >7 days old)
- _inbox/2026-03-28-security-observation.md — 10 days old
- _inbox/2026-03-30-vendor-note.md — 8 days old
→ Action: Triage now or discard
```

---

### Check 2: Missing Standard Metadata

**What:** Files in content directories that lack a YAML frontmatter block.

**Directories to scan:**
- `2-Knowledge/HowTo/`
- `2-Knowledge/Decisions/`
- `2-Knowledge/References/`
- `1-Projects/` (overview files only)

**How:** Read each file's first 20 lines. If no `type:` YAML frontmatter field found, flag it.

**Output format:**
```
🏷️ MISSING METADATA (X files)
- 2-Knowledge/HowTo/deployment-guide.md — no metadata block
- 2-Knowledge/Decisions/old-decision.md — no metadata block
→ Action: Add standard block at top of each file
```

---

### Check 3: Stale Active Files

**What:** Files with `status: active` but `updated:` date > 90 days ago.

**Exemptions:** Files with `status: archived` or `status: superseded` are exempt — terminal-status pages are intentionally frozen and should not be flagged as stale. Only flag `active` files.

**Output format:**
```
⏰ STALE ACTIVE FILES (X files, >90 days since update)
- 2-Knowledge/HowTo/onboarding-process.md — last updated 2025-10-15 (173 days ago)
→ Action: Review each — update, archive, or mark as stable
```

---

### Check 4: Orphaned Files

**What:** Files with no inbound links from any other file.

**How:** Check if each scanned file appears in any other file as a markdown link `[text](path)`.

**Output format:**
```
🔗 ORPHANED FILES (X files — no inbound links)
- 2-Knowledge/HowTo/old-tool-setup.md
→ Action: Link from a relevant doc or archive
```

---

### Check 5: Context Size & Optimization Review

**What:** Instruction files that are getting too large, and whether an optimization review is overdue.

**Flag if:**
- Any instruction module > 300 lines → candidate for splitting
- Core files (PHILOSOPHY.md, general.md) > 500 lines → review needed
- `.last-optimization-review` doesn't exist or is >30 days old → suggest full review

**How:**
```bash
wc -l _config/config.md _meta/instructions/general.md PHILOSOPHY.md
wc -l _meta/instructions/*.md | sort -rn | head -10
cat .last-optimization-review 2>/dev/null || echo "No review recorded"
```

**Output format:**
```
🧠 CONTEXT SIZE & OPTIMIZATION
⚠️ general.md: 450 lines (approaching 500 — consider modularizing)
✓ PHILOSOPHY.md: 120 lines
⚠️ Last optimization review: 45 days ago (>30 — run full review)
→ Action: Load optimization-review.md and run full review
```

If optimization review is overdue, suggest loading `_meta/instructions/optimization-review.md` for the full protocol.

---

### Check 6: Non-Timestamped Filenames

**What:** Files in content directories whose names don't start with `YYYY-MM-DD-`.

**Scope:** `0-Ideas/`, `1-Projects/`, `2-Knowledge/`, `3-Journal/`, `4-Private/`, `5-Publishing/`, `_inbox/`, `_seeds/` (if present).

**Exceptions (skip):** Any file named `README.md`, `PHILOSOPHY.md`, `WIKI-LOG.md`, `AGENTS.md`, `CLAUDE.md`, or any file in `_config/`, `_meta/`.

**How:**
1. For each non-compliant file, get its first-commit date:
   ```bash
   git log --diff-filter=A --follow --format="%ad" --date=short -- <file> | tail -1
   ```
2. If the file has no git history (untracked), use today's date.
3. Propose rename: `YYYY-MM-DD-original-name.md` where the date is the first-commit date.

**Output format:**
```
📅 NON-TIMESTAMPED FILENAMES (X files)
- 2-Knowledge/some-concept.md → 2026-03-15-some-concept.md (first commit: 2026-03-15)
- 0-Ideas/startup-idea.md → 2026-04-10-startup-idea.md (first commit: 2026-04-10)
→ Action: Rename files — retroactive, uses git first-commit date as timestamp
```

This check is retroactive by design. Run it periodically to catch files added before the rule was enforced.

---

### Check 7: Raw File Paths (Not Wiki Links)

**What:** File paths written as plain text or backtick code spans in table cells or prose that should be wiki links. Catches two sub-cases:

1. **Format issue** — path exists but is written as `` `path/to/file.md` `` or `path/to/file.md` instead of `[[path/to/file]]`
2. **Broken link** — an existing `[[wikilink]]` where the target file does not exist

**Scope:** All `.md` files in content directories. Common in "Where" or "Source" table columns, and in files imported from external tools.

**How to detect format issues:**
```bash
grep -rn '`[^`]*/[^`]*\.md`' --include="*.md" <directories>
```

**How to detect broken links:** grep for `\[\[[^\]]+\]\]`, extract the path (before any `|`), strip extension, check if the file exists.

**Conversion rule:**
- Strip the `.md` extension
- Wrap in `[[` and `]]`
- Full vault-relative path preferred: `[[1-Projects/foo/bar]]`

**Output format:**
```
🔗 RAW PATHS / BROKEN LINKS (X items)
FORMAT: 2-Knowledge/doc.md:12 — `1-Projects/foo/bar.md` → [[1-Projects/foo/bar]]
BROKEN: 2-Knowledge/doc.md:8 — [[1-Projects/old-name]] → target not found
→ Action: Convert format issues in-place; broken links need manual resolution
```

---

## Output: Lint Report

After running all checks, compile a summary:

```
📋 WIKI LINT REPORT — YYYY-MM-DD
- ✅ Checks run: 7
- ⚠️ Issues found: X
- 🔴 Requires action: X

[Each check's output]
```

Append one line to `WIKI-LOG.md`:
```
## [YYYY-MM-DD] lint | X issues found — stale: X, missing metadata: X, orphaned: X, timestamps: X, paths: X
```

---

## Cadence

**Recommended:** Monthly, or whenever the system feels messy.

During the training period, running lint is a good way to discover what conventions need to be established.
