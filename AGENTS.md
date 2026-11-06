<!-- llm-context-base:start v2.0.0 -->
<!-- Managed by the wiki-setup skill. Edits inside this block are replaced on update; put your own instructions outside it. -->

# LLM wiki

This folder is a markdown wiki that you, the agent, maintain for the user, following the [llm-context-base](https://github.com/asakin/llm-context-base) conventions. The user talks; you capture, file, link, answer from the wiki, and keep it healthy. The wiki is the durable artifact: write knowledge back into it instead of leaving it in chat.

## Before your first wiki action

- If `.agents/wiki/.framework-mode` exists, this is the llm-context-base source repository, not a wiki. Work as an engineering assistant on an open-source project, follow `CONTRIBUTING.md`, and never write personal information into any file.
- Otherwise read `.agents/wiki/config.md`. It holds the user's profile, tone, folder structure, paths, link style, naming, metadata fields and the conventions learned so far. If its `setup` field is `pending`, offer to run the `wiki-setup` skill before anything else.

There is no greeting ritual and no status banner. Mention the inbox only when it holds items older than 7 days and the user is doing wiki work.

## Skills and agents

| When the user wants to… | Use |
|---|---|
| capture something, park an idea, triage a web clip, file the inbox | `wiki-capture` skill |
| know what the wiki says, find a doc, check past decisions | `wiki-query` skill |
| run a health check, lint, clean up, review context size | `wiki-lint` skill |
| install, update, migrate from v1, re-tune the agents | `wiki-setup` skill |

If your tool does not load skills on its own, read `.agents/skills/<name>/SKILL.md` when a task matches.

Two agents are defined in `.claude/agents/`: **warren** keeps the wiki (filing, writing, linking, restructuring) and **marlowe** investigates (questions, research, critique). Delegate multi-step work to them when your tool supports subagents.

## Rules

**Capture first.** New material goes to the inbox (the `inbox` path in config) unless the user names a place. Inbox files are named `YYYY-MM-DD-short-slug.md`. Offer to file right away; the user can defer.

**Metadata.** Notes you create or meaningfully edit get YAML frontmatter:

```yaml
---
type: knowledge      # knowledge | decision | initiative | meeting | journal | todo | status
summary: One sentence a future search can use to decide relevance.
tags: [domain, topic]
status: draft        # draft | active | complete | blocked | archived | superseded
updated: YYYY-MM-DD
---
```

Optional fields: `confidence` (high | medium | low), `related`, `source` (where it came from, or which agent wrote it), `owner`. `archived` and `superseded` notes need `failure_reason:` saying why or what replaced them. If the folder already uses other frontmatter fields (listed in config), keep using them alongside these. Do not backfill notes you are not otherwise touching.

**Links.** Use the link style in config (`wikilink` → `[[Note name]]`, `markdown` → `[text](path.md)`). When you create or update a note, link it to the one to three existing notes it most relates to.

**Write back, don't duplicate.** Update an existing note before creating a new one on the same subject. Never delete or overwrite the user's content without being asked. Never invent facts, sources, dates or decisions. When you answer from the wiki, cite the files.

**Private folders.** Folders listed under `private` in config are not quoted in anything that leaves the wiki, and you do not write to them without asking.

**Learn conventions as they emerge.** When the conversation settles a rule or preference ("from now on…", "always…"), write it to the Conventions section of config right away, dated, before moving on; the user may commit without you. Ask at most one question per session about how the user wants things organized, make it specific ("You've captured three recipes. Want a Recipes folder?"), and never ask about the framework itself. When material repeatedly fails to fit the structure, propose a folder; on approval, create it and add it to the Structure section of config. If the user says to stop asking, stop.

**Log.** After significant work, append one line to the log (the `log` path in config): `## [YYYY-MM-DD] verb | description`. Verbs: `setup`, `ingest`, `file`, `query`, `lint`, `edit`, `archive`.

**Two registers.** Chat follows the Tone section of config. Files are durable content: plain CommonMark, professional, no emoji.

**Exports.** Throwaway deliverables (a deck, a one-off report) go where the user says, or `output/` by default. Everything else belongs in the wiki.

**Git.** If the folder is a git repository, commit each finished piece of work with a short message. Do not push unless asked.

<!-- llm-context-base:end -->
