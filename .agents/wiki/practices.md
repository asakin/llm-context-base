# Wiki practices

The common ground llm-context-base brings to every wiki. Each folder is ahead on some of these and behind on others; setup records, for each one, whether the folder already does it, adopts it, adapts it to its house rules, or declines it. That record is the Practices section of `.agents/wiki/config.md`, and it outranks the defaults below.

Adopting a practice never means breaking what the folder already built. If the house already has an equivalent, keep the house's. If a practice can only fit by changing something the house relies on (a sync, a hook, a publisher's rules), adapt it or decline it, and say which.

## Capture first, file later

**Why:** hesitating over where something belongs is how it gets lost. **Default:** new material lands in the inbox and is filed within about a week; items older than that come up for triage. **Adapting:** use the house's intake folder and its rules for what may be committed or cited. **Skill:** `wiki-capture`.

## Fold before you create

**Why:** a wiki with three half-pages on one subject answers worse than one with a single full page. **Default:** before creating a page, look for an existing one on the subject and update it; extract durable claims, decisions and corrections, never file a raw dump. **Adapting:** follow the house's hierarchy and placement rules for any page you do create. **Skill:** `wiki-capture`.

## Answers become pages

**Why:** the wiki should grow from use, not only from intake; an answer that took real synthesis is knowledge. **Default:** after such an answer, offer to save it as a page or fold it into an existing one. **Skill:** `wiki-query`.

## Cite, date and admit gaps

**Why:** an answer is only as good as the reader's ability to check it. **Default:** cite every page used with its date, warn when a source is stale, and say "nothing found" instead of filling the gap. **Adapting:** if a sync rewrites dates, judge age from evidence that survives it (dates in titles, history). **Skill:** `wiki-query`.

## Decisions carry their outcomes

**Why:** a decision record is most valuable later, when the same kind of choice comes up again. **Default:** decisions record the options, the rationale, and an Outcome section filled in once results are known; before a new decision, related past decisions come up first, failures included. **Adapting:** use the house's decision format if it has one, adding an outcome section if it lacks one. **Skills:** `wiki-query`, template `decision.md`.

## Nothing retires without a trail

**Why:** a reader who lands on a dead page should find out why it died and where to go. **Default:** archived or superseded pages say why (`failure_reason`) or what replaced them. **Adapting:** where frontmatter belongs to another tool, put the trail in the page's first line or the house's own archive mechanism. **Skill:** `wiki-lint`.

## Drafts get finished

**Why:** a draft nobody can find or trust helps nobody. **Default:** a page stays a draft until it's complete, filed and linked; the agent nudges toward finishing, and placeholders and long-idle drafts come up in health checks. **Skills:** `wiki-capture`, `wiki-lint`.

## Every page can be found

**Why:** agents and people decide what to read from names and one-line summaries; a page with neither is invisible. **Default:** each page has a one-sentence `summary` in frontmatter and links to the one to three pages it most relates to, and something links to it. **Adapting:** where frontmatter belongs to another tool, use the house's equivalent (a description field, the first paragraph, the parent page's one-line child list). **Skill:** `wiki-lint`.

## Conventions are written down when they're decided

**Why:** a rule agreed in chat is gone by the next session. **Default:** "from now on…" goes into the Conventions section of `config.md` at once, dated, where every agent reads it.

## Health checks end in fixes

**Why:** a report of 900 broken links changes nothing; the top five fixes, offered, do. **Default:** a regular health check (monthly, or when the wiki feels messy) of stale items, placeholders, orphans, broken links and the house's own rules, reported as fixes ranked by value. **Adapting:** turn off checks the house makes meaningless and add checks for house rules worth enforcing, in the Lint section of config. **Skill:** `wiki-lint`.

## A second pair of eyes

**Why:** whoever writes a page is the worst person to audit it. **Default:** periodically check pages for contradictions, stale claims, weak evidence and duplicates, separately from maintaining them. **Agent:** Marlowe.

## Instructions stay small

**Why:** every always-loaded instruction costs context in every session, and instruction files grow quietly. **Default:** keep what agents load every session (all `AGENTS.md` files in play plus `config.md`) measured and compact; anything task-specific belongs in a skill. **Skill:** `wiki-lint`.

## The same procedures in every agent

**Why:** a wiki maintained by several agents drifts unless they all follow the same procedures. **Default:** procedures live as Agent Skills in `.agents/skills/` and rules in `AGENTS.md`, which most agents read; agents that can't see the skills set themselves up (see `AGENTS.md`).

## Private stays private

**Why:** a wiki holds things its owner wouldn't publish. **Default:** folders listed as private are never quoted in anything that leaves the wiki and aren't written to without asking. **Adapting:** include folders the house already keeps personal or agent-owned.
