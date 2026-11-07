<!-- llm-context-base:start v2.0.0 -->
<!-- Managed by the wiki-setup skill. Edits inside this block are replaced on update; put your own instructions outside it. -->

## LLM wiki (llm-context-base)

This folder is a markdown wiki that you, the agent, maintain for the user, following the [llm-context-base](https://github.com/asakin/llm-context-base) conventions. The user talks; you capture, file, link, answer from the wiki, and keep it healthy. The wiki is the durable artifact: write knowledge back into it instead of leaving it in chat.

### Before your first wiki action

- If `.agents/wiki/.framework-mode` exists, this is the llm-context-base source repository, not a wiki. Work as an engineering assistant on an open-source project, follow `CONTRIBUTING.md`, and never write personal information into any file. If the user wants a wiki of their own, explain that it is set up in its own folder (a new one or an existing notes folder) as the README's quick start describes, not in this clone.
- Otherwise read `.agents/wiki/config.md`. If its `setup` field is `pending`, offer to run the `wiki-setup` skill before anything else.

There is no greeting ritual and no status banner. Mention the inbox only when it holds items older than 7 days and the user is doing wiki work.

### Set yourself up

Any agent working here should be able to use the wiki skills, whatever tool it runs in. Before your first wiki task, check that you can:

- **The skills are in `.agents/skills/` but your tool doesn't load them:** read `.agents/skills/<name>/SKILL.md` yourself when a task matches the table below. If your tool loads skills from another folder, offer to link the `wiki-*` skills there so they load automatically next time, and tell the user what you linked.
- **`.agents/skills/` is missing or has no `wiki-*` skills** (they were installed somewhere this checkout doesn't have, or the folder was copied without hidden files): get them from the llm-context-base release named in the first line of this block (`https://github.com/asakin/llm-context-base`, tag `vX.Y.Z`), follow them from there for this session, and offer to run `wiki-setup` to install them in the folder.

### What llm-context-base adds

A shared set of wiki practices, listed in `.agents/wiki/practices.md`: capture first, fold before you create, answers become pages, cite and date, decisions carry their outcomes, nothing retires without a trail, drafts get finished, every page can be found, conventions are written down, health checks end in fixes, a second pair of eyes, small instructions, the same procedures in every agent, private stays private. The Practices section of `config.md` says how each one applies in this folder; read `practices.md` when a task touches one you're unsure of.

### The folder's own rules come first

Many folders had conventions before llm-context-base arrived: instruction files, a sync to another tool, link or naming rules, a frontmatter format, an intake folder. Setup recorded them, and how llm-context-base adapted to each, in the House rules section of `config.md`.

- Where `config.md` and this block disagree, `config.md` wins. The rules below are defaults for whatever the house rules don't cover.
- Every other instruction you were given (the rest of this file, `CLAUDE.md`, rules from parent folders, the user's home or their organization) is a house rule too. Follow it and never edit the files it comes from. If one stands in the way of what the user asked, say which rule and ask.

### Skills and agents

| When the user wants to… | Use |
|---|---|
| capture something, park an idea, triage a web clip, file the inbox | `wiki-capture` skill |
| know what the wiki says, find a doc, check past decisions | `wiki-query` skill |
| a health check, a cleanup, to know what needs attention | `wiki-lint` skill |
| maintenance: merge, split, archive, restructure, tidy prose | `wiki-keep` skill |
| research, an audit, a page verified against its sources | `wiki-investigate` skill |
| install, update, migrate from v1, re-tune the agents | `wiki-setup` skill |

The skills were adapted to this folder when they were installed (paths, link style, frontmatter, house checks), so follow them as written here rather than from memory of the originals. If your tool does not load skills on its own, read `.agents/skills/<name>/SKILL.md` when a task matches.

Two agents are defined in `.claude/agents/`: **warren** keeps the wiki (the `wiki-keep` skill) and **marlowe** investigates (the `wiki-investigate` skill). Delegate multi-step work to them when your tool supports subagents; otherwise follow the skill yourself.

### Defaults

**Capture first.** New material goes to the inbox (the `inbox` path in config) unless the user names a place. Inbox files are named `YYYY-MM-DD-short-slug.md`. Offer to file right away; the user can defer.

**Metadata.** Follow the `frontmatter` setting in config. When it is `llm-context-base`, notes you create or meaningfully edit get YAML frontmatter:

```yaml
---
type: knowledge      # knowledge | decision | initiative | meeting | journal | todo | status
summary: One sentence a future search can use to decide relevance.
tags: [domain, topic]
status: draft        # draft | active | complete | blocked | archived | superseded
updated: YYYY-MM-DD
---
```

Optional fields: `confidence` (high | medium | low), `related`, `source` (where it came from, or which agent wrote it), `owner`. `archived` and `superseded` notes need `failure_reason:` saying why or what replaced them. Keep any other fields a note already has. Do not backfill notes you are not otherwise touching. When `frontmatter` is `host`, another tool writes it: never add or change fields. When it is `none`, write none.

**Links.** Use the link style in config (`wikilink` → `[[Note name]]`, `markdown` → `[text](path.md)`), and any link rules in the house rules. When you create or update a note, link it to the one to three existing notes it most relates to.

**Write back, don't duplicate.** Update an existing note before creating a new one on the same subject. Never delete or overwrite the user's content without being asked. Never invent facts, sources, dates or decisions. When you answer from the wiki, cite the files.

**Private folders.** Folders listed under `private` in config are not quoted in anything that leaves the wiki, and you do not write to them without asking.

**Learn conventions as they emerge.** When the conversation settles a rule or preference ("from now on…", "always…"), write it to the Conventions section of config right away, dated, before moving on; the user may commit without you. Ask at most one question per session about how the user wants things organized, make it specific ("You've captured three recipes. Want a Recipes folder?"), and never ask about the framework itself. When material repeatedly fails to fit the structure, propose a folder; on approval, create it and add it to the Structure section of config. If the user says to stop asking, stop.

**Two registers.** Chat follows the Tone section of config. Files are durable content in the folder's own style; by default plain CommonMark, professional, no emoji.

**Exports.** Throwaway deliverables (a deck, a one-off report) go where the user says, or `output/` by default. Everything else belongs in the wiki.

**Git.** If the folder is a git repository, commit each finished piece of work with a short message. Do not push unless asked.

<!-- llm-context-base:end -->
