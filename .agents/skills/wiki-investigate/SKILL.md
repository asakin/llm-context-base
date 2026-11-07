---
name: wiki-investigate
description: Investigate an llm-context-base wiki. Use when asked to research a topic or source and map it onto what the wiki already says, audit or critique notes for contradictions, stale claims, weak evidence, duplicates and gaps, or verify a page against its primary sources. Read-heavy; proposes changes instead of rewriting notes. Marlowe follows this skill; any agent can.
---

# Investigating the wiki

Find out what is true, what the wiki already says, and where the two disagree. Be skeptical, specific and useful; the point is a wiki the user can trust, not a performance. The wiki's version of events is a client's story: check it, follow the evidence past the version anyone would prefer, and report straight, including when the answer is that the wiki was right.

Read `.agents/wiki/config.md` first (house rules, especially which sources to trust and which dates can be believed). To answer a question from the wiki, follow `wiki-query`.

## What investigating covers

- **Research:** a topic or source, separating what the wiki already knows from what new sources add.
- **Critique:** contradictions between notes or with newer sources, stale or superseded claims, uncited or overconfident statements, duplicate notes, concepts mentioned everywhere but missing a note.
- **Verification:** a page checked claim by claim against the sources it cites or should cite.

## How to work

1. Pin down the question or review scope.
2. Scan the wiki first: file names, then metadata, then the few notes that matter.
3. For research, read the sources given or search when appropriate. Build an evidence map: source, date, claim, confidence, conflicts, affected notes. Treat source quality, freshness and licensing as part of the result.
4. Ask of every suspect claim: compared with what source, note or newer evidence is this wrong, stale or weak?
5. Report, then propose the durable updates.

## Writing

Read-only by default. When findings should become wiki content, write them as an inbox note (`source: marlowe` or your own name) for the keeper or the user to file, unless the user asks you to edit notes directly and the edit is narrow and safe. Stay out of `private` folders unless asked.

## Report shape

For anything beyond a quick lookup:

- **What the wiki says**, with citations.
- **New evidence**, with sources.
- **Findings**, each with evidence (paths and quotes), severity (high, medium, low), and the recommended action.
- **Observations**: lower-confidence concerns, labelled as such rather than overstated.

Never invent contradictions, sources or gaps. If you are unsure, say how unsure.
