---
name: wiki-query
description: Answer questions from an llm-context-base wiki with citations. Use when the user asks "what do we know about…", "how do we…", "what did we decide about…", "what's the status of…", "find the doc for…", "has this been documented?", or is about to make a decision that past decisions could inform.
---

# Answering from the wiki

Read `.agents/wiki/config.md` first: the Structure table says where each kind of note lives, and the House rules say what dates and fields can be trusted (a sync may rewrite `updated`).

## Search

1. **Classify the question.** Process, decision, project status, meeting, reference, or several at once. Pick the folders from the Structure table.
2. **Scan before reading.** List file names, then read only the frontmatter (`summary`, `tags`, `status`, `updated`) of candidates. File names and summaries often answer the question.
3. **Read one to three notes in full.** For a very long note, read the section that matters.
4. **Cross-type questions** ("what's happening with deployment this week?") pull from each relevant folder separately, then combine the answer by type.
5. Deprioritize `archived` and `superseded` notes unless the question is about history; follow `failure_reason` to the replacement.

## Answer

Synthesize, then cite every note used with its path and `updated` date:

```text
Sources:
- Knowledge/deployment-process.md (updated 2026-03-15)
- Decisions/database-choice.md (updated 2026-02-20)
```

Warn when a cited note is stale: more than 30 days old for status or active-project notes, more than 90 days for reference material.

If nothing matches, say so plainly ("I couldn't find anything on X") and offer to capture it in the inbox or start a note. Never answer as if a document exists when it doesn't.

If the answer took real synthesis across several notes, offer to save it back into the wiki as a note.

## Past decisions

When the user is weighing options ("should we…", "I'm deciding between…") or starts a decision note, look for decisions in the same domain (by tags or topic). Surface the ones with a filled-in Outcome section, and especially failures or mixed outcomes and their "Constraints discovered":

```text
Related past decisions:
- choosing-postgresql-over-mongodb.md: succeeded. Lesson: match the database to the data model.
- switching-to-kubernetes.md: mixed. Constraint: migration took 3x the estimate because of stateful services.
```
