---
name: wiki-setup
description: Start a new llm-context-base wiki, or install, update or migrate it in an existing folder of markdown notes, and tune the wiki's agents. Use when the user says "start a new wiki", "set up llm-context-base here", "turn this folder into an LLM wiki", "update llm-context-base", "migrate from v1", "re-tune Warren/Marlowe", or when .agents/wiki/config.md says setup is pending.
---

# Setting up llm-context-base

llm-context-base joins a folder the way a symbiont joins a host: it adapts to the conventions already there, brings what the folder lacks, and leaves the folder better at what it was already doing. In an existing folder it never moves, renames or rewrites notes, and never edits the folder's own instruction files.

**Talk the user through it.** This is their first look at the system. Before each step, say in a sentence or two what you are about to do and why. When you ask a question, say what depends on the answer. Keep survey numbers to the few that explain a decision; the user doesn't need counts for their own sake.

## 1. Find out what kind of folder this is

If the user named a folder ("start a new wiki in ~/notes"), work there: create it if it doesn't exist. Otherwise the target is the current folder.

| What you find in the target | Mode |
|---|---|
| `.agents/wiki/.framework-mode` | A clone of the llm-context-base source repo, meant for contributors. Stop, and offer to start a fresh wiki in a new folder or to set it up in an existing notes folder instead. |
| `AGENTS.md` containing `<!-- llm-context-base:start` | **Update** (also used to re-tune the agents) |
| `_config/config.md` and `_meta/instructions/` | **Migrate from v1** |
| Markdown notes, an `.obsidian/` folder, or other content | **Existing folder** |
| Nothing, or only a README or `.git` | **Fresh start** |

If the user's words and the folder disagree (they asked for a fresh wiki but the folder holds notes, or the reverse), say what you found and ask which they meant.

**Fresh start:** if the folder isn't a git repository, offer `git init`; history is how the user undoes anything an agent does. **Existing folder:** if it's a git repository with uncommitted changes, suggest committing first so setup's changes can be reviewed and reverted on their own; if it isn't one, suggest a backup, and go on when the user is ready.

## 2. Get the framework files

Fetch the framework into a temporary directory, never into the target. Use the same version as this skill: if you read it from a URL, take the git ref from that URL (`main` in the README's link, a branch or tag otherwise); if the user gave a local path or named a fork, branch or tag, use that; when an installed copy runs an update, use `main`, which always holds the latest release.

```bash
REPO=https://github.com/asakin/llm-context-base
REF=main   # or the ref the skill came from
SRC=$(mktemp -d) && git clone --quiet --depth 1 --branch "$REF" "$REPO" "$SRC"
```

Without git, download `$REPO/archive/refs/heads/$REF.tar.gz` (or `refs/tags/` for a tag) and unpack it instead. Tell the user which version you're installing: the `vX.Y.Z` in the first line of `$SRC/AGENTS.md`. In **update** mode, compare it with the version in the target's `<!-- llm-context-base:start vX.Y.Z -->` line; if they match, say it's up to date and offer only the agent re-tuning in step 8. Otherwise show the release notes (`$REPO/releases/tag/vX.Y.Z`) before continuing.

Read `$SRC/AGENTS.md`, `$SRC/.agents/wiki/config.md`, `$SRC/.agents/wiki/practices.md` and the six `wiki-*` skills before going on: they are the practices and defaults you are about to fit to this folder.

## 3. Learn the house rules

Before installing anything, learn how this folder already works. You are the newcomer.

There are always house rules, even in an empty folder. The instructions your harness has already loaded into this session (from this folder, the folders above it, the user's home, or an organization's managed policy) are house rules too. You don't need to go looking for them, and you can't override them: adapt to whatever they say, and leave enforcing them to the user's own guardrails. The folder may hold more that no harness loads, so in an existing folder also read:

- **Instruction files in the folder** that weren't loaded into this session, such as a README or CONTRIBUTING that tells people or agents how to write here.
- **Tooling that touches notes:** sync scripts and the CI that runs them (a wiki mirrored from Notion, Outline, Confluence or a docs site), git hooks (`.git/hooks/`, a `pre-commit` config, `scripts/`), linters and formatters (`.markdownlint*`, `.prettierrc`, `.editorconfig`), publishing configs (Hugo, MkDocs, Docusaurus, Jekyll, Quartz), `.gitignore`, Obsidian's `.obsidian/` settings and plugins.
- **The notes themselves:** sample up to 200. Note the link style (count `[[…]]` against `[…](….md)`, and how spaces and paths are written), the frontmatter fields in use and whether a tool generates them, file naming, folder hierarchy (does a parent page have a same-named folder of children?), and any markup that only works in one renderer.

From this, work out what each house rule implies for an agent writing here. Folders differ widely; some of the kinds of rules you may find:

- **Publishing:** a static site (MkDocs, Docusaurus, Hugo, Quartz) needs a `title` or `draft` field, a page listed in a nav file, or files under `content/`; a mirror of Notion, Outline or Confluence owns the frontmatter and rejects some markup.
- **Note-taking method:** Zettelkasten timestamp IDs and flat folders, Johnny.Decimal or PARA numbering, Logseq `journals/` and `pages/` with `key:: value` properties, Dendron or Foam dot-hierarchies (`project.alpha.notes.md`), daily notes as the only intake.
- **Metadata:** tags written inline as `#tag` rather than in frontmatter, Dataview inline fields, a fixed set of properties per note type, no frontmatter at all.
- **Process:** decisions as numbered ADRs with a fixed template, changes only through pull requests, CODEOWNERS on some folders, generated files nobody edits by hand.
- **Language and style:** a spelling or language rule, a formatter that wraps lines, a style guide.
- **Boundaries:** encrypted or gitignored folders, folders owned by a person or another agent, an instruction file nobody may edit.

Don't assume any of these; record only what the folder actually shows.

## 4. Fit llm-context-base to the house

For each thing llm-context-base brings, find the house's equivalent and decide:

| llm-context-base brings | Look for the house's |
|---|---|
| An inbox for captures | Intake folder: `raw/`, `Inbox/`, `_inbox/`, `00 Inbox/`, a daily-notes folder, or whatever the instruction files describe |
| YAML frontmatter (`type`, `summary`, `tags`, `status`, `updated`) | Frontmatter fields and who writes them |
| A link style | Link format the folder or its publisher requires |
| A naming rule | Naming per folder |
| Note templates | Existing templates (Obsidian Templates or Templater folder, a templates directory) |
| Private folders | Folders the instruction files or `.gitignore` keep personal or agent-owned |
| Lint checks (see the `wiki-lint` skill) | Linters, hooks and publisher rules that already check notes, and rules a lint check would contradict |
| Committing finished work | Commit and push rules |

Decide each row this way:

- **The house has an equivalent and the difference doesn't matter:** adopt the house's. The user's established practice wins over ours.
- **The house has an equivalent and ours is meaningfully better:** propose ours, say concretely what the user gains, and let them choose. Improving their practice is the point, but it's their call.
- **The house has nothing:** bring ours.
- **A house rule blocks something llm-context-base needs:** say which rule and ask. Never edit the folder's own instruction files, hooks or tooling to get around it. If the house has a mechanism for proposing changes (for example, writing a proposed `AGENTS.md` next to the real one), use it, and say what that means: agents only read the real `AGENTS.md`, so llm-context-base stays switched off until someone accepts the proposal. Let the user choose between that and approving the edit now.

Then go through the practices in `practices.md` the same way. For each one, decide whether the folder already does it (**in place**: say how), will take llm-context-base's default (**adopted**), needs fitting to the house rules (**adapted**: say how), or can't take it without breaking something the house relies on (**declined**: say why). This is what the user gains from installing, so make it concrete: name the pages, folders or rules each practice touches here.

In an existing folder, show the user both results and wait for a yes before installing: a short table of house rules (topic, house rule, what llm-context-base will do here), then the practices grouped as already in place, being added, adapted, and declined. They become the House rules and Practices sections of `config.md`. In a fresh start, skip the table: say in a sentence that llm-context-base's defaults apply within the rules the user's tools already set, name any default the user is likely to care about (for example wikilinks, which suit Obsidian, or markdown links, which suit GitHub), and record the defaults in the House rules section.

## 5. Install

List the files you will add or replace and wait for a yes. In a fresh start, describe them in a sentence instead (the rules in `AGENTS.md`, the skills and settings in hidden folders, an inbox); a new user has no use for the file list. Then, from `$SRC`:

- **`AGENTS.md`:** copy the block from `<!-- llm-context-base:start` through `<!-- llm-context-base:end -->`. If the target has an `AGENTS.md`, replace its existing block or, if it has none, put the block at the top; keep everything else in the file as it is. If the target has no `AGENTS.md`, create one with just the block. If a house rule forbids editing `AGENTS.md`, follow step 4's last rule.
- **`CLAUDE.md`:** must contain the line `@AGENTS.md`. Create the file if missing; otherwise add the line at the top if it isn't there. A `.claude/CLAUDE.md` gets the same treatment if it exists instead of a root one.
- **`.agents/skills/wiki-*`:** replace each `wiki-*` directory whole. Leave other skills alone.
- **`.agents/wiki/practices.md`:** copy it, replacing any older version.
- **`.agents/wiki/templates/`:** copy each shipped template, overwriting files of the same name. The user's own templates in that folder stay. Skip this if the house has its own templates and the user chose them in step 4.
- **`.agents/wiki/config.md`:** copy only if it doesn't exist. Never overwrite it.
- **`.claude/agents/warren.md` and `marlowe.md`:** if a file of that name exists without the `llm-context-base:agent` comment, it is the user's own: ask before touching it. Otherwise replace everything above the `<!-- llm-context-base:local -->` line and keep the local section below it.
- **Claude Code skills:** Claude Code reads only `.claude/skills/`. If it doesn't exist, link it: `ln -s ../.agents/skills .claude/skills`. If it exists as a folder, link each wiki skill inside it: `ln -s ../../.agents/skills/wiki-capture .claude/skills/wiki-capture` (and so on). If symlinks fail, copy the directories and say an update will refresh them.

Nothing else from `$SRC` is copied. Delete `$SRC` when you're done.

## 6. Adapt the skills to the house

The shipped skills describe the defaults. Each installed copy must describe this folder, so that an agent following it never has to translate. Edit the six `wiki-*` skills in place:

- Replace llm-context-base's defaults with the house's wherever a skill mentions them: the intake folder, link style and syntax, the metadata rule (when `frontmatter` is `host` or `none`, every instruction to set or read `type`, `summary`, `status` or `updated` becomes the house's equivalent, such as inline tags, a property syntax or a nav entry, or is removed), naming, where new notes go, decision format, the private folders.
- In `wiki-lint`, delete the checks turned off for this folder, change thresholds, and write the house checks out in full as numbered checks of their own.
- In `wiki-capture`, replace the filing steps that don't apply with the house's intake workflow, and point to the house's templates if those were chosen.
- In `wiki-query`, say which dates and fields can be trusted here.
- Keep the frontmatter `name` and `description`. Don't shorten a skill for its own sake; the goal is a skill that is right for this folder, not a smaller one.

Put one line under each skill's frontmatter: `<!-- Adapted to this folder by wiki-setup on YYYY-MM-DD from llm-context-base vX.Y.Z. The record of what was adapted is the House rules, Practices and Lint sections of .agents/wiki/config.md. -->`. In **update** mode the fresh copies are adapted again from those sections of `config.md`, so keep them complete. In a **fresh start** the skills need no adaptation beyond the inbox path, if it changed.

## 7. Write the config

Fill in `.agents/wiki/config.md` from steps 3 and 4:

- **Frontmatter keys:** `inbox`, `link_style`, `naming`, `frontmatter` (`llm-context-base`, `host` when another tool writes it, or `none`), `private`, and `setup:` set to today.
- **House rules:** the table from step 4, one row per topic, plus any other house rule an agent writing here must know.
- **Practices:** one row per practice with its status here and, for in place, adapted and declined, a few words on how or why.
- **Structure:** the top-level folders and what each holds, in a sentence each.
- **Lint:** how the `wiki-lint` checks apply here. Turn off checks the house makes meaningless (for example the metadata check when `frontmatter` is `host`), change thresholds that don't fit, and add checks for house rules worth enforcing (for example "wikilinks that match several pages are refused by the publisher"). Give each a one-line reason.
- **Conventions:** anything the user decided during setup, dated.

Do not add frontmatter to notes during setup.

**Fresh start:** there is nothing to survey. Create the inbox. Offer a starter layout in one short paragraph, and create it only on a yes: `Projects/` (one folder per project with an `_overview.md`), `Knowledge/` (with `HowTo/`, `Decisions/`, `References/`), `Journal/` and `Private/` (both in `private`). Otherwise the structure grows as the user captures things.

**Migrate from v1:** after the install, showing each change first:

1. **Config:** copy About You, Conversation Tone, Training Log and Your Conventions from `_config/config.md`, plus everything in `_config/context.md`, into the matching sections of `config.md` (training-log entries become dated Conventions lines). Copy tool entries from `_config/tools.md` into Tools. Set `inbox: _inbox/`, `private: [3-Journal/, 4-Private/]`, `preserve_sources` from the old setting with `sources: _sources/`, `link_style: markdown` unless the notes say otherwise, `naming: as-found`. Keep `1-Projects/` to `4-Private/` and describe them in Structure.
2. **Templates:** copy any template in `_meta/templates/` that the user changed or added into `.agents/wiki/templates/` under a name the framework doesn't ship.
3. **Old framework files:** remove, after confirming the list: `.cursorrules`, `.cursor/rules/bootstrap.mdc`, `.windsurfrules`, `.github/copilot-instructions.md`, `.claude/CLAUDE.md`, `_config/`, `_meta/instructions/`, `_meta/templates/`. The v1 `AGENTS.md` and `CLAUDE.md` were shims too (they start with "STEP 0: Framework mode check"): remove that text and keep only the new block plus anything the user added. Offer to remove the v1 template's own files if still there: `PHILOSOPHY.md`, `docs/`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `migrate-to-yaml-frontmatter.py`, `WIKI-LOG.md`, and the framework half of `README.md` (everything from `<!-- llm-context-base:framework-readme -->` down).
4. **Metadata:** v1.0 notes use `**Type:** …` lines and some v1.1 notes use `- **Type:** …` bullets. Run `python3 .agents/skills/wiki-setup/scripts/migrate-frontmatter.py . --dry-run`, show the list, and run it without `--dry-run` only on a yes.

## 8. Tune the agents

Ask in a single message, all optional:

- What is this wiki for, and who reads it?
- What may Warren do without asking (file the inbox, fix links, merge notes, rename files)?
- Which sources should Marlowe trust or avoid, and how blunt should critiques be?
- Anything about tone in chat?

Write the answers into the `<!-- llm-context-base:local -->` section of `warren.md` and `marlowe.md` as short rules, and the profile and tone answers into About You and Tone in `config.md`. When re-tuning, show the current local sections and edit them; don't start over.

## 9. Offer pi extensions

Only if `pi` is on the PATH (`command -v pi`); otherwise don't mention pi.

- **pi-rebrief** reloads `AGENTS.md` and other context files into a running pi session, so a session started before setup picks up the new rules without restarting. Offer it if `pi list` doesn't show it: `pi install git:github.com/asakin/pi-rebrief`, then `/reload` and `/rebrief` in the running session.
- **The pi agents extension** lets Warren and Marlowe run in pi. Offer it only if the install source below is filled in. On a yes, install it and tell the user to `/reload`. If it reads agents from somewhere other than `.claude/agents/`, link the two agent files there.

<!-- TODO(pi-extension): fill in before releasing v2.0.0. -->
- Name: PI_EXTENSION_NAME
- Install: `pi install PI_EXTENSION_SOURCE`
- Agent path it reads: PI_AGENT_PATH

## 10. Finish

1. **Commit.** If it's a git repository: make sure `AGENTS.md`, `CLAUDE.md` and `.agents/` aren't ignored; offer to add `private` folders to `.gitignore` if the house rules allow; commit with `chore: set up llm-context-base vX.Y.Z` (or `update to`).
2. **Reload.** The agent session that ran setup loaded its instructions before the block existed. Tell the user to start a new session (or `/rebrief` in pi) so every rule applies.
3. **Show what changed for them.** Don't report survey statistics or run a lint. In a short message:
   - **What you can do now that you couldn't before:** three to five things, each with a phrase to try that uses this folder's real content (a real project name, a real topic). For example "Capture this: …" landing in their intake folder, "What do we know about <topic they have notes on>?" answered with citations, "File my inbox", "Should we <a decision their notes touch on>?" surfacing past decisions.
   - **How it fits their house rules:** one or two sentences on the most important adaptations, and which practices the wiki gained that it didn't have before.
   - **One concrete improvement to start with:** pick a single specific thing you noticed during the survey that you can fix now, and offer to do it ("Four pages are still placeholders, starting with *What we build*. Want me to draft it from what the wiki already says?"). One offer, not a list.
4. **Obsidian:** if there's an `.obsidian/` folder, mention the Web Clipper template (`https://github.com/asakin/llm-context-base/blob/main/assets/clipper-template.json`, imported with its folder set to the inbox) and kepano/obsidian-skills for Obsidian syntax.
