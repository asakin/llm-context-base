---
type: template
summary: Health-check pass for the wiki — surfaces stale metadata, missing standard blocks, orphaned files, and stale inbox items.
tags: [meta, maintenance]
status: active
updated: 2026-04-09
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

**What:** Files in content directories that lack the metadata block (`**Type:**`, `**Summary:**`, `**Tags:**`).

**Directories to scan:**
- `2-Knowledge/HowTo/`
- `2-Knowledge/Decisions/`
- `2-Knowledge/References/`
- `1-Projects/` (overview files only)

**How:** Read each file's first 20 lines. If no `**Type:**` field found, flag it.

**Output format:**
```
🏷️ MISSING METADATA (X files)
- 2-Knowledge/HowTo/deployment-guide.md — no metadata block
- 2-Knowledge/Decisions/old-decision.md — no metadata block
→ Action: Add standard block at top of each file
```

---

### Check 3: Stale Active Files

**What:** Files with `**Status:** active` but `**Updated:**` date > 90 days ago.

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

## Output: Lint Report

After running all checks, compile a summary:

```
📋 WIKI LINT REPORT — YYYY-MM-DD
- ✅ Checks run: 5
- ⚠️ Issues found: X
- 🔴 Requires action: X

[Each check's output]
```

Append one line to `WIKI-LOG.md`:
```
## [YYYY-MM-DD] lint | X issues found — stale: X, missing metadata: X, orphaned: X
```

---

## Cadence

**Recommended:** Monthly, or whenever the system feels messy.

During the training period, running lint is a good way to discover what conventions need to be established.
