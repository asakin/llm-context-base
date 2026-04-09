# Tools

- **Type:** knowledge
- **Summary:** Declares local tools the AI may install on your machine to enable output rendering and other capabilities. Not committed as binaries — just a manifest.
- **Tags:** #meta #tools #config
- **Status:** active
- **Updated:** 2026-04-09

---

## How This Works

This file is the manifest for local tools the system uses. The tools themselves are installed on your machine, not committed to the repo — the same way `package.json` declares dependencies without committing `node_modules`.

On first session (or when a tool shows as "not installed"), your AI will offer to install it with a single command. You approve, it installs, it never asks again.

Local tool binaries go in `_tools/` (gitignored). Global installs stay wherever the package manager puts them.

---

## Tools

### Marp
- **Purpose:** Renders markdown to slides (HTML, PDF, PPTX) and design docs to PDF
- **Install:** `npm install -g @marp-team/marp-cli`
- **Trigger:** User asks for slides, PDF output, presentations, or design docs
- **Status:** not installed
- **Docs:** https://marp.app

---

## Adding Tools

To add a tool, append an entry in this format:

```markdown
### [Tool Name]
- **Purpose:** [What it does, when the AI uses it]
- **Install:** [exact command to install]
- **Trigger:** [what the user says that should invoke this tool]
- **Status:** not installed
- **Docs:** [link]
```

Your AI will check this file when it needs to render output and offer to install missing tools.

---

## Notes

- Tools are installed on your machine, not in the repo
- `_tools/` is gitignored — local binaries never get committed
- If you clone this repo on a new machine, your AI will re-offer to install missing tools
- Distros may pre-populate this file with tools specific to their use case
