# Knowledge Query Module

- **Type:** template
- **Summary:** How to answer natural language queries by routing to the right files and synthesizing answers with citations.
- **Tags:** #meta #knowledge
- **Status:** active
- **Updated:** 2026-04-09

---

## Purpose

This module enables natural language queries across all content — not just knowledge articles, but decisions, initiatives, meetings, and more. It replaces manual folder navigation.

**Load this module when user asks:**
- "How do we [process]?" / "What's our process for [X]?"
- "What do we know about [X]?"
- "What did we decide about [X]?"
- "What's the status of [X]?"
- "Find me docs about [X]"
- "Has this been documented?"
- "Where's the doc for [X]?"

---

## Query Routing Table

Match the question type to the right starting directory:

| Question Type | Primary Location | Secondary |
|--------------|-----------------|-----------|
| "How do we [process]?" | `2-Knowledge/HowTo/` | `2-Knowledge/References/` |
| "How to [tactical task]?" | `2-Knowledge/HowTo/` | `2-Knowledge/References/` |
| "What's the guide for [X]?" | `2-Knowledge/References/` | `2-Knowledge/HowTo/` |
| "What did we decide about [X]?" | `2-Knowledge/Decisions/` | — |
| "What's in flight on [topic]?" | `1-Projects/` | — |
| "What happened in [meeting]?" | `3-Journal/` | — |
| "What's the current status?" | Root (`WIKI-LOG.md`) | `1-Projects/` |

> **Note:** This routing table will expand during training as you add directories. Your AI should update it when new content areas are created.

---

## Search Strategy

### Step 1: Classify the query
What type is this? Which domain tag applies? Which directory does the routing table point to?

### Step 2: Check the index
Read `README.md` in the target directory to understand what files exist. File names often answer the question without reading content.

### Step 3: Scan summaries
If files have the metadata block (`**Summary:**`), read only those lines first. Pick 1-3 files that match based on summary and tags.

### Step 4: Read relevant files
Read the 1-3 most relevant files in full. For very large files (500+ lines), focus on the first major section.

### Step 5: Synthesize and cite
Return a synthesized answer with source citations:

```
**Source:** `2-Knowledge/HowTo/deployment-process.md`
**Updated:** 2026-03-15 | **Type:** knowledge

[Answer here]
```

For multiple sources:
```
**Sources:**
- `2-Knowledge/HowTo/deployment-process.md` (Updated: 2026-03-15)
- `2-Knowledge/Decisions/database-choice.md` (Updated: 2026-02-20)

[Answer synthesized from both sources]
```

---

## Freshness Warnings

If a file's `**Updated:**` date is more than:
- **30 days** for time-sensitive content (status, active projects) → warn
- **90 days** for reference content (guides, architecture docs) → warn

```
⚠️ This file was last updated X days ago. Content may be stale.
```

---

## "Nothing Found" Behavior

If no matching file is found:

1. Tell the user clearly: "I couldn't find documentation for [X]."
2. Offer to capture it: "Would you like me to add this to the inbox so we can document it?"
3. If it seems like a missing process doc: "This might be worth creating as a knowledge article."

**Do NOT hallucinate documentation that doesn't exist.** Cite only real files.

---

## Cross-Type Queries

Some queries span multiple types. For example: "What's happening with deployment this week?"

This could pull from:
- `2-Knowledge/` (tagged with relevant domain)
- `1-Projects/` (active initiatives in that area)
- `3-Journal/` (recent meeting notes)

For cross-type queries:
1. Identify which types are relevant
2. Route to each source independently
3. Synthesize a unified view, organized by type

---

## Tags as Filters

Use tags to filter relevance when searching across multiple files:
- Domain tag match → strong signal of relevance
- Status filter: `archived` files can usually be deprioritized unless explicitly asked about history

---

## Decision Learning Loop

When a user is about to make a new decision (evaluating options, choosing between approaches, making a trade-off), **proactively check `2-Knowledge/Decisions/` for past decisions with recorded outcomes.**

### How it works:

1. **Detect decision context** — User says "should we...", "I'm deciding between...", "we need to choose...", or starts a new decision record
2. **Search past decisions** — Scan `2-Knowledge/Decisions/` for decisions in the same domain (match by tags or topic)
3. **Surface relevant precedents** — If past decisions have an `## Outcome` section filled in, surface them:

```
📋 Related past decisions:
- `choosing-postgresql-over-mongodb.md` — Outcome: succeeded
  Key lesson: "Match the database to the data model, not the hype"
- `switching-to-kubernetes.md` — Outcome: mixed
  Constraint discovered: "Migration took 3x longer than estimated due to stateful services"
```

4. **Include failure constraints** — Past decisions that failed or had mixed outcomes are especially valuable. Their "Constraints Discovered" sections should actively inform the new decision.

### Why this matters:

The system doesn't just remember what you decided — it learns from how those decisions played out. Over time, your decision records become operational experience, not just documentation.

---

## Integration with Inbox

If the user asks about something that doesn't exist yet, offer to capture it:

```
I couldn't find documentation for [X]. Would you like me to:
1. Add it to _inbox/ as a capture for later
2. Create a knowledge article now
```
