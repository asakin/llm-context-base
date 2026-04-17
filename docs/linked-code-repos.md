# Linking Your Wiki to Code Repos

If you're a developer, some of your `1-Projects/` entries correspond to real code repositories — not just wiki pages, but actual git repos that live somewhere like `~/projects/`.

This doc describes a pattern for connecting them.

---

## The pattern

When a project entry in `1-Projects/` has a corresponding code repo, create a multi-root workspace file that opens both together in a single editor window.

The workspace puts **the code repo first, the wiki second.** You're working on code — the wiki is context, not the primary root.

```json
{
  "folders": [
    { "name": "my-project",       "path": "/path/to/my-project" },
    { "name": "my-wiki",          "path": "/path/to/my-wiki" }
  ]
}
```

If the project has a companion repo (Homebrew tap, extension registry, etc.), add it between the main project and the wiki.

---

## Why it works

Your AI agent has full wiki context while editing the code repo. `CLAUDE.md` / `.cursorrules` in the code repo points back to the wiki for architectural decisions. You stop switching windows.

The code repo also gets a context file that explains how it fits into the larger system — something that would otherwise get lost every time you open a fresh session.

---

## Workspace file placement

Save the `.code-workspace` file in the project's `1-Projects/` folder:

```
1-Projects/
  my-project/
    _overview.md
    my-project.code-workspace   ← here
```

Open it with:
- VS Code: `code 1-Projects/my-project/my-project.code-workspace`
- Cursor: `cursor 1-Projects/my-project/my-project.code-workspace`

---

## Context files in the code repo

Add two files to the code repo so any AI opened there understands the bigger picture:

**`CLAUDE.md`** — read by Claude Code automatically. Explain what the project is, what it's part of, what's stubbed, and where the source of truth lives.

**`.cursorrules`** — read by Cursor automatically. Same content, shorter format.

Both should point back to the wiki: *"The person with full context is [wiki location]. When in doubt, open Claude Code there."*

---

## Obsidian plugin dev: symlinks

If the project is an Obsidian plugin, symlink it into the vault's plugins folder rather than cloning it:

```bash
ln -s ~/projects/my-plugin /path/to/vault/.obsidian/plugins/my-plugin
```

This way you develop in one place and Obsidian picks up changes live. Pair with the [hot-reload plugin](https://github.com/pjeby/hot-reload) for sub-second feedback.

---

## Asking your AI to set this up

During project creation, your AI should ask:

1. **Cursor or VS Code?** (determines the open command, same file format)
2. **Does the code repo exist?** If not, propose a name and create it.

From there it scaffolds: clones (or creates) the repo, generates the workspace file, writes `CLAUDE.md` and `.cursorrules` in the code repo, and adds the project entry to the wiki.

---

## Extension territory

The scaffold logic (workspace file generation, repo creation, context file templates) is editor-specific and belongs in an extension, not in the core framework. Core stays editor-agnostic.

The concept — a 1-Projects/ entry linked to an external code repo — is the load-bearing idea. The workspace file is just one expression of it.
