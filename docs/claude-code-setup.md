# Claude Code Setup

This system is designed to work with Claude Code as the AI layer. This page covers recommended settings to make the experience smooth.

---

## The Key Insight

This is a **pile of markdown files in Git**. It's not production code. It's not getting deployed. You can always `git revert`.

The default Claude Code permission model is designed for codebases where edits matter and bash commands can be dangerous. For a markdown knowledge base, that level of caution creates friction without adding safety. The settings below are calibrated for this use case.

Claude Code now also has native project subagents, so this template does not need to rely on prompt tricks to keep agents focused on wiki maintenance. Project-specific subagents live in `.claude/agents/` and are checked into the repo for everyone using the wiki.

---

## Included wiki-maintainer subagents

This repo ships Claude Code project subagents in `.claude/agents/`:

| Subagent | Use it for |
|----------|------------|
| `wiki-librarian` | Filing inbox items, updating pages, normalizing metadata, preserving citations |
| `wiki-researcher` | Researching topics or sources, producing synthesis, identifying pages to update |
| `wiki-critic` | Read-only critique: contradictions, stale claims, weak evidence, conceptual gaps |
| `wiki-gardener` | Structural cleanup: merges, splits, backlinks, metadata normalization |
| `wiki-editor` | Prose, tone, terminology, and readability without changing underlying claims |

These agents are framed around the same principle:

> You maintain the user's LLM Wiki. The wiki is the durable artifact. Your job is to improve it, not replace it.

Claude Code discovers project subagents from `.claude/agents/`. They are loaded at session start, so restart Claude Code after adding or editing agent files directly on disk. You can invoke them by name in natural language, with an agent @-mention in Claude Code, or by running a whole session as one with `claude --agent wiki-librarian`.

Custom subagents run in their own context window with their own system prompt and tool access. That makes them useful for focused, self-contained wiki maintenance tasks, especially work that would otherwise flood the main conversation with search output, source reading, or health-check findings.

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

## Hooks

Claude Code hooks let you run shell commands at specific lifecycle events. Two patterns worth knowing for a wiki setup:

### Re-run session start after /compact

When you run `/compact`, Claude Code compresses the conversation context. Without intervention, the next response won't know it needs to re-run the session start protocol.

**The sentinel pattern** — PostCompact writes a flag file; UserPromptSubmit reads it on the next prompt and injects the re-init instruction:

```json
{
  "hooks": {
    "PostCompact": [{
      "matcher": "manual",
      "hooks": [{
        "type": "command",
        "command": "touch /tmp/wiki-post-compact && printf '{\"systemMessage\": \"Wiki context compacted — re-init will fire on your next message.\"}\\n'"
      }]
    }],
    "UserPromptSubmit": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash .claude/hooks/post-compact-check.sh"
      }]
    }]
  }
}
```

Create `.claude/hooks/post-compact-check.sh`:
```bash
#!/bin/bash
SENTINEL="/tmp/wiki-post-compact"
if [ -f "$SENTINEL" ]; then
  rm -f "$SENTINEL"
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"Context was just compacted. Re-run the session start protocol now before responding to anything else."}}'
fi
```

Note: `PostCompact` does not support `hookSpecificOutput.additionalContext` — only `UserPromptSubmit` and `PostToolUse` do. The sentinel pattern is the correct workaround.

### Track wiki files read per session

Useful for knowing how much of the wiki was consulted during a session:

```json
"PostToolUse": [{
  "matcher": "Read",
  "hooks": [{
    "type": "command",
    "command": "jq -r '.tool_input.file_path // empty' | grep -E '\\.md$' >> /tmp/claude-wiki-reads-${SESSION_ID}.log 2>/dev/null || true"
  }]
}]
```

---

## Tips

**During setup, let Claude offer to auto-allow.** When a new command gets prompted, Claude can add it to the allow list for you. Just say yes when it asks.

**The settings file is committed.** If you clone this vault on another machine, the settings come with it. You don't need to reconfigure.

**If you add plugins or distros with real tooling**, revisit this file. The defaults above are calibrated for a markdown-only vault. A plugin that makes network requests or runs build tools may warrant tighter controls.
