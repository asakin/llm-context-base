# Context Optimization Review

- **Type:** template
- **Summary:** Periodic review of instruction file sizes and context efficiency - keeps the system lean as your wiki grows.
- **Tags:** #meta #maintenance #optimization
- **Status:** active
- **Updated:** 2026-04-09

---

## Purpose

As your wiki grows, instruction files tend to grow with it - new conventions get logged, modules get extended, templates accumulate sections. Left unchecked, this bloats the context window and slows down every session.

This protocol reviews the system's own operating efficiency. It's part of the self-maintaining philosophy: the wiki doesn't just maintain your content, it maintains its own instruction set.

**Load this module when:**
- User says "optimize", "context efficiency", "review what we're loading"
- Lint flags that `.last-optimization-review` is >30 days old
- You notice files being re-read multiple times in a session

---

## When to Review

### Monthly Check (Recommended)

At lint time, check the `.last-optimization-review` file in the project root. If it doesn't exist or is >30 days old, suggest a review:

> "It's been [X] days since the last context optimization review. Want me to check if the instruction files are still lean?"

### Event-Driven Triggers

Flag a review during a session if you notice:

1. **Large files loaded** - Any instruction file >300 lines or core file >500 lines
2. **Repeated reads** - Reading the same large file 3+ times in one session
3. **Session feels slow** - User or AI notice context limits being approached

### User-Requested

User can always ask:
- "Review what we're loading at session start"
- "Are we being efficient with context?"
- "Optimize the instructions"

---

## Review Process

### Step 1: Analyze Current State

Check file sizes for all core and instruction files:

```bash
# Core files loaded at session start
wc -l _config/config.md _config/context.md _meta/instructions/general.md PHILOSOPHY.md README.md

# All instruction modules
wc -l _meta/instructions/*.md | sort -rn

# Templates (loaded on demand, but check for bloat)
wc -l _meta/templates/*.md | sort -rn
```

### Step 2: Identify Issues

Flag anything that exceeds thresholds:
- Core files (config.md, general.md, PHILOSOPHY.md): >500 lines each
- Instruction modules: >300 lines each
- Templates: >100 lines each
- Total session start load: >800 lines combined

### Step 3: Propose Changes

Present findings to the user:

```
📊 Context Optimization Review - YYYY-MM-DD

Session start files: [X] lines total
- config.md: [X] lines [✓ or ⚠️]
- general.md: [X] lines [✓ or ⚠️]
- context.md: [X] lines [✓ or ⚠️]
- PHILOSOPHY.md: [X] lines [✓ or ⚠️]

Instruction modules:
- knowledge-query.md: [X] lines [✓ or ⚠️]
- knowledge-lint.md: [X] lines [✓ or ⚠️]
- [etc.]

Recommendations:
- [Specific suggestions if any issues found]
- [Or: "No changes needed - system is lean"]
```

### Step 4: Implement (With Approval)

If changes are needed, common actions include:
- **Split large files** into focused modules (e.g., a 400-line general.md could split into general.md + session-protocol.md)
- **Move content to conditional loading** - if a section of config.md is only relevant during training, move it to a training-specific module
- **Compact verbose sections** - remove redundant examples, tighten language
- **Remove unused modules** - if a module was never triggered, consider removing or archiving it

Always get user approval before restructuring instruction files.

### Step 5: Document

```bash
# Record review date
date +%Y-%m-%d > .last-optimization-review
```

Append to WIKI-LOG.md:
```
## [YYYY-MM-DD] optimization | Session start: [X] lines, [changes made or "no changes needed"]
```

---

## Success Metrics

**Healthy system:**
- Session start consistently ~600-800 lines
- Instruction modules each <300 lines
- Files read once per session, not repeatedly
- Clear patterns for when to load which module

**Warning signs:**
- Session start creeping toward 1000+ lines
- Modules growing past 300 lines without being split
- Same file re-read 3+ times in a session
- Confusion about which module to load for a given task

---

## When NOT to Optimize

**Don't optimize prematurely:**
- The system is working well and sessions feel fast
- You're not hitting context limits
- Files are being read appropriately (once each, on demand)

Optimization has a cost (time, complexity, risk of breaking things). Only optimize when there's a clear benefit. A few extra lines in a file that works well is better than a perfectly optimized file that got broken in the process.

---

## Related

- [knowledge-lint.md](knowledge-lint.md) - Check 5 flags file sizes and triggers this review
- [general.md](general.md) - Session Start Protocol defines what gets loaded
- `_config/config.md` - Core Behaviors mentions JIT loading
