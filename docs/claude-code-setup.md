# Claude Code Setup

This system is designed to work with Claude Code as the AI layer. This page covers recommended settings to make the experience smooth.

---

## The Key Insight

This is a **pile of markdown files in Git**. It's not production code. It's not getting deployed. You can always `git revert`.

The default Claude Code permission model is designed for codebases where edits matter and bash commands can be dangerous. For a markdown knowledge base, that level of caution creates friction without adding safety. The settings below are calibrated for this use case.

---

## Recommended settings.json

Create `.claude/settings.json` in your vault root (this file is already included in the repo as a starting point):

```json
{
  "cleanupPeriodDays": 90,
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": [
      "Bash(git:*)",
      "Bash(gh:*)",
      "Bash(python:*)",
      "Bash(python3:*)",
      "Bash(marp:*)",
      "Bash(jq:*)",
      "WebSearch"
    ]
  }
}
```

### What each setting does

| Setting | Why |
|---------|-----|
| `defaultMode: acceptEdits` | File reads and edits go through without prompting. You're editing markdown, not deploying code. |
| `cleanupPeriodDays: 90` | Keeps 3 months of transcript history instead of the default 30 days. For a knowledge base where sessions build on each other, more history = better context continuity. |
| `Bash(git:*)` | All git operations auto-approved. You're going to be committing a lot. |
| `Bash(gh:*)` | GitHub CLI — needed for PR creation, issue management. |
| `Bash(python:*)` / `Bash(python3:*)` | Required if you use the nightly Idea Runner or any other vault scripts. |
| `Bash(marp:*)` | Auto-approved if you use Marp for slide/PDF output. Remove if you don't use it. |
| `Bash(jq:*)` | JSON processing — used by some vault scripts. |

---

## What about riskier operations?

`acceptEdits` auto-approves file reads and edits, but **bash commands that aren't in the allow list still prompt**. That's intentional — this vault may eventually have plugins or distros that call real tools, and you want a gate on novel bash commands.

If you want zero prompts (including bash), you can set `defaultMode: bypassPermissions`. This is fine for a pure markdown vault, but be thoughtful if you're adding plugins or distros that run external tools.

---

## Adding domains for WebFetch

If you use web clipping or research features, add the domains you want to allow:

```json
"WebFetch(domain:example.com)"
```

Claude Code will still prompt for unlisted domains — you can approve them one-off and add them to the list after.

---

## Tips

**During setup, let Claude offer to auto-allow.** When a new command gets prompted, Claude can add it to the allow list for you. Just say yes when it asks.

**The settings file is committed.** If you clone this vault on another machine, the settings come with it. You don't need to reconfigure.

**If you add plugins or distros with real tooling**, revisit this file. The defaults above are calibrated for a markdown-only vault. A plugin that makes network requests or runs build tools may warrant tighter controls.
