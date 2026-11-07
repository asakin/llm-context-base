# Contributing to llm-context-base

Every installed copy of llm-context-base is an experiment. As the agent adapts a wiki to someone's needs, useful patterns turn up: a template, a skill, a lint check, a better way to adopt an existing folder. Those patterns are what this project grows from.

## What makes a good contribution

Contribute structure, not content. Your notes stay in your wiki; what helps others is the pattern.

Good contributions:

- **Templates** for note types the set doesn't cover (retrospectives, reading notes, vendor evaluations)
- **Skills** that teach the agent a broadly useful behavior, or improvements to the four existing ones
- **Setup improvements**, especially for folder layouts and conventions that setup doesn't recognize yet
- **Agent improvements** to Warren and Marlowe
- **Fixes** where an instruction doesn't work well with a particular agent or model

Not contributions: personal content, company-specific conventions, or changes that only make sense for one wiki.

Genericize before you submit. A `Recipes/` template with cuisine and prep-time fields becomes a "collection item" template with user-defined categories and attributes. If a change requires knowing what your wiki is about, it's a local customization; if it works regardless of domain, it's a contribution.

## How to contribute

Open an [issue](https://github.com/asakin/llm-context-base/issues) describing the pattern: the problem it solves, how you implemented it, why it would help others. Or fork the repo, add the genericized version, and open a pull request.

## Repository layout

The repository is the source of what setup installs. Setup copies only these paths into a user's folder:

| Path | Installed as |
|---|---|
| `AGENTS.md`, between the `llm-context-base:start` and `:end` markers | The block in the user's `AGENTS.md` |
| `.agents/skills/wiki-*` | Replaced whole on every update, then re-adapted to the folder from `config.md` |
| `.agents/wiki/practices.md` | Replaced on every update |
| `.agents/wiki/templates/*` | Overwritten by file name; user templates with other names are kept |
| `.agents/wiki/config.md` | Copied only if the user has none; never overwritten |
| `.claude/agents/warren.md`, `marlowe.md` | Replaced above the `llm-context-base:local` line |

Everything else (`README.md`, `docs/`, `examples/`, `assets/`, `.github/`) stays in this repository. If you add a framework file, add it to the install list in `.agents/skills/wiki-setup/SKILL.md` and to this table.

Keep the always-loaded part small: the `AGENTS.md` block and a fresh `config.md` together should stay well under 300 lines. Anything needed only for some tasks belongs in a skill. Skill frontmatter uses only `name` and `description`, so every agent that supports Agent Skills can load it.

## Working on the framework with an agent

A clone of this repository is a contributor checkout, not a wiki. The committed file `.agents/wiki/.framework-mode` tells agents (including Warren and Marlowe) to work as engineering assistants on an open-source project: no setup, no personalizing, no personal information in files that ship to every user. Setup never copies that file, so installed wikis don't have it.

To try the repository itself as a wiki, delete the file locally and don't commit the deletion. To test setup properly, open an agent in a scratch folder (empty for a fresh start, or a copy of a real vault) and ask it to set up llm-context-base from your working copy by giving it the local path; setup uses a source you name instead of the latest release.

## Commits and checks

Commit messages use [Conventional Commits](https://www.conventionalcommits.org/) prefixes: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`, with `!` for breaking changes. CI runs markdownlint and a link check on every pull request; run them locally with:

```bash
npx markdownlint-cli2 "**/*.md"
lychee --no-progress .
python3 .agents/skills/wiki-setup/scripts/migrate-frontmatter.py --self-test
```

## Releasing

1. Update the version in the `llm-context-base:start` line of `AGENTS.md` and the `llm-context-base:agent` lines of both agents.
2. Make sure `grep -rn "TODO(pi-extension)" .agents` returns nothing.
3. Merge to `main`, tag `vX.Y.Z`, and publish a GitHub release with notes. Setup installs the newest `v*` tag, so the tag is what users get.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be kind; this project exists because people shared their patterns.
