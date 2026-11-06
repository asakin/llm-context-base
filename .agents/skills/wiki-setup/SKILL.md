---
name: wiki-setup
description: Start a new llm-context-base wiki, or install, update or migrate it in an existing folder of markdown notes, and tune the wiki's agents. Use when the user says "start a new wiki", "set up llm-context-base here", "turn this folder into an LLM wiki", "update llm-context-base", "migrate from v1", "re-tune Warren/Marlowe", or when .agents/wiki/config.md says setup is pending.
---

# Setting up llm-context-base

The target is the folder the user is working in. Setup adds a small set of framework files, learns how the folder is already organized, and never moves, renames or rewrites the user's notes without asking.

## 1. Find out what kind of folder this is

If the user named a folder ("start a new wiki in ~/notes"), work there: create it if it doesn't exist. Otherwise the target is the current folder.

| What you find in the target | Mode |
|---|---|
| `.agents/wiki/.framework-mode` | A clone of the llm-context-base source repo, meant for contributors. Stop, and offer to start a fresh wiki in a new folder or to set it up in an existing notes folder instead. |
| `AGENTS.md` containing `<!-- llm-context-base:start` | **Update** (also used to re-tune the agents) |
| `_config/config.md` and `_meta/instructions/` | **Migrate from v1** |
| Markdown notes, an `.obsidian/` folder, or other content | **Existing folder** |
| Nothing, or only a README or `.git` | **Fresh start** |

If the user's words and the folder disagree (they asked for a fresh wiki but the folder holds notes, or the reverse), say what you found and ask which they meant before going on.

**Fresh start:** if the folder isn't a git repository, offer `git init`; history is how the user undoes anything the agent does. **Existing folder:** if it's a git repository with uncommitted changes, suggest committing first so setup's changes can be reviewed and reverted on their own; if it isn't one, mention that a commit or backup before setup is a good idea, and go on when the user is ready.

## 2. Get the framework files

Fetch the latest release into a temporary directory, never into the target:

```bash
REPO=https://github.com/asakin/llm-context-base
TAG=$(git ls-remote --tags --refs --sort=-v:refname "$REPO" 'v*' | head -1 | sed 's|.*refs/tags/||')
SRC=$(mktemp -d) && git clone --quiet --depth 1 --branch "$TAG" "$REPO" "$SRC"
```

Without git, download `$REPO/archive/refs/tags/$TAG.tar.gz` and unpack it instead. If the user names a source (a local clone, a branch, a fork), use that as `$SRC` instead of the latest release, and say so. In **update** mode, compare `$TAG` with the version in the target's `<!-- llm-context-base:start vX.Y.Z -->` line; if they match, say it's up to date and offer only the agent re-tuning in step 6. Otherwise show the release notes (`$REPO/releases/tag/$TAG`) before continuing.

## 3. Tell the user what will change, then install

List the files you will add or replace and wait for a yes. Then, from `$SRC`:

- **`AGENTS.md`:** copy the block from `<!-- llm-context-base:start` through `<!-- llm-context-base:end -->`. If the target has an `AGENTS.md`, replace its existing block or, if it has none, put the block at the top; keep everything else in the file as it is. If the target has no `AGENTS.md`, create one with just the block.
- **`CLAUDE.md`:** must contain the line `@AGENTS.md`. Create the file if missing; otherwise add the line at the top if it isn't there. Leave the rest alone. A `.claude/CLAUDE.md` gets the same treatment if it exists instead of a root one.
- **`.agents/skills/wiki-*`:** replace each `wiki-*` directory whole. Leave any other skills in `.agents/skills/` alone.
- **`.agents/wiki/templates/`:** copy each shipped template, overwriting files of the same name. The user's own templates in that folder stay.
- **`.agents/wiki/config.md`:** copy only if it doesn't exist. Never overwrite it.
- **`.claude/agents/warren.md` and `marlowe.md`:** if the target already has a file of that name without the `llm-context-base:agent` comment, it is the user's own: stop and ask before touching it. Otherwise replace everything above the `<!-- llm-context-base:local -->` line with the new version and keep the local section below it.
- **Claude Code skills:** Claude Code reads only `.claude/skills/`. If `.claude/skills` doesn't exist, link it: `ln -s ../.agents/skills .claude/skills`. If it exists as a folder, link each wiki skill inside it instead: `ln -s ../../.agents/skills/wiki-capture .claude/skills/wiki-capture` (and so on). On Windows, or if symlinks fail, copy the directories and tell the user an update will refresh the copies.

Nothing else from `$SRC` is copied: not its README, docs, license, assets or CI. Delete `$SRC` when you're done.

## 4. Learn the folder (fresh, existing and v1 modes)

Survey before you write config, and show the user what you found:

- **Structure:** top-level folders, what each seems to hold, and note counts. Write them to the Structure table in `config.md`.
- **Inbox:** reuse an existing inbox-like folder (`Inbox/`, `_inbox/`, `00 Inbox/`…) as `inbox`; otherwise use `inbox/`.
- **Log:** reuse an existing `log.md`-style changelog if there is one; otherwise `log.md`.
- **Link style:** count `[[…]]` against `[…](….md)` across notes; the majority sets `link_style`.
- **Frontmatter:** sample up to 200 notes and list the fields in use. Fields other than `type`, `summary`, `tags`, `status`, `updated` go in `extra_frontmatter`. Do not add frontmatter to notes now; it gets added as notes are touched.
- **Naming:** if most notes start with `YYYY-MM-DD-`, set `naming: date-prefixed`; if folders differ, `as-found`; else `descriptive`.
- **Private:** propose folders that look personal (`Journal`, `Diary`, `Private`, `Personal`, `Health`, `Finance`) for `private` and let the user confirm.

Then fill in the frontmatter of `config.md` and set `setup:` to today's date.

**Fresh start:** there is nothing to survey. Create the inbox and the log. Offer a starter layout in one short paragraph, and create it only on a yes: `Projects/` (one folder per project with an `_overview.md`), `Knowledge/` (with `HowTo/`, `Decisions/`, `References/`), `Journal/` and `Private/` (both in `private`). Otherwise the structure grows as the user captures things.

## 5. Migrate from v1

Do these after step 3, showing each change first:

1. **Config:** copy About You, Conversation Tone, Training Log and Your Conventions from `_config/config.md`, plus everything in `_config/context.md`, into the matching sections of `.agents/wiki/config.md` (training-log entries become dated Conventions lines). Copy tool entries from `_config/tools.md` into Tools. Set `inbox: _inbox/`, `private: [3-Journal/, 4-Private/]`, `preserve_sources` from the old setting with `sources: _sources/`, `link_style: markdown` unless the survey says otherwise, `naming: as-found`, and `log` to `2-Knowledge/log.md` if it exists, else `WIKI-LOG.md`. Keep `1-Projects/` to `4-Private/` as they are and describe them in Structure.
2. **Templates:** copy any template in `_meta/templates/` that the user changed or added into `.agents/wiki/templates/` under a name the framework doesn't ship.
3. **Old framework files:** remove, after confirming the list: `.cursorrules`, `.cursor/rules/bootstrap.mdc`, `.windsurfrules`, `.github/copilot-instructions.md`, `.claude/CLAUDE.md`, `_config/`, `_meta/instructions/`, `_meta/templates/`. The v1 `AGENTS.md` and `CLAUDE.md` were shims too (they start with "STEP 0: Framework mode check" and point at `_config/config.md`): remove that shim text and keep only the new block plus anything the user added. Offer to remove the v1 template's own files too if they're still there: `PHILOSOPHY.md`, `docs/`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `migrate-to-yaml-frontmatter.py`, and the framework half of `README.md` (everything from `<!-- llm-context-base:framework-readme -->` down).
4. **Metadata:** v1.0 notes use `**Type:** …` lines and some v1.1 notes use `- **Type:** …` bullets. Run `python3 .agents/skills/wiki-setup/scripts/migrate-frontmatter.py . --dry-run`, show the list, and run it without `--dry-run` only on a yes.

## 6. Tune the agents

Ask in a single message, all optional:

- What is this wiki for, and who reads it?
- What may Warren do without asking (file the inbox, fix links, merge notes, rename files)?
- Which sources should Marlowe trust or avoid, and how blunt should critiques be?
- Anything about tone in chat?

Write the answers into the `<!-- llm-context-base:local -->` section of `warren.md` and `marlowe.md` as short rules, and the profile and tone answers into About You and Tone in `config.md`. When re-tuning, show the current local sections and edit them; don't start over.

## 7. Offer the pi extension

If `pi` is on the PATH (`command -v pi`) and the install source below is filled in, offer: "You use pi. Install the PI_EXTENSION_NAME extension so Warren and Marlowe work in pi too?" On a yes, run the install command and tell the user to `/reload` any running pi session. If the extension reads agents from somewhere other than `.claude/agents/`, link the two agent files there. If `pi` isn't installed, don't mention it.

<!-- TODO(pi-extension): fill in before releasing v2.0.0. -->
- Name: PI_EXTENSION_NAME
- Install: `pi install PI_EXTENSION_SOURCE`
- Agent path it reads: PI_AGENT_PATH

## 8. Finish

1. Append `## [YYYY-MM-DD] setup | llm-context-base vX.Y.Z (mode)` to the log.
2. If it's a git repository: make sure `AGENTS.md`, `CLAUDE.md` and `.agents/` aren't ignored; offer to add the `private` folders to `.gitignore`; commit with `chore: set up llm-context-base vX.Y.Z` (or `update to`).
3. If there's an `.obsidian/` folder, mention the Web Clipper template (`https://github.com/asakin/llm-context-base/blob/main/assets/clipper-template.json`, import it in Web Clipper settings and set its folder to the inbox) and kepano/obsidian-skills for Obsidian-specific syntax.
4. Tell the user what was added and three things to try: "Capture this: …", "What do we know about …?", "Lint the wiki."
