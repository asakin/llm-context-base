# General Instructions

This is the core instruction module for the AI assistant. It defines the session start protocol, module routing, and foundational behaviors.

---

## Session Start Protocol

At the start of every session, follow these steps in order:

### Step 1: Read Configuration
Read `_config/config.md`. This contains the user's profile, system settings, and training log.

### Step 2: Calculate Phase
Using the Training Start Date and Training Period Days from `_config/config.md`, determine the current phase:

- **Training** → Day 0 to Training Period Days
- **Cooldown** → Training Period Days to Training Period Days + 14
- **Established** → After cooldown

Adjust your behavior accordingly (see `_config/config.md` for phase-specific behaviors).

### Step 3: Load Context
- **Training phase:** Read `PHILOSOPHY.md`, this file, `_config/context.md`, `README.md`
- **Cooldown phase:** Read `PHILOSOPHY.md`, this file, `_config/context.md`
- **Established phase:** Read this file and `_config/context.md` only (you know the system by now)

### Step 4: Check Inbox
Check `_inbox/` for files older than 7 days. If any exist, surface them:

```
📥 Inbox triage needed: X files older than 7 days
- _inbox/YYYY-MM-DD-topic.md (X days old)
→ Action: File to final location, update, or discard
```

### Step 5: Training Check (Training Phase Only)
If in training phase, review:
- What did you learn in the last session? (check Training Log)
- What questions should you ask this session?
- Are there patterns emerging that suggest new directories or conventions?

### Step 6: Output Session Summary (REQUIRED)

**You MUST output the session summary before responding to anything else.** This is the gate — the protocol is not complete until this block is printed.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SESSION START
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase:     [training / cooldown / established] (Day X of Y)
Config:    [ready / ⚠ About You section not filled in / ⚠ Training Start Date not set]
Inbox:     [clear / ⚠ X files older than 7 days]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If config is not filled in, add a note prompting the user to complete it before continuing. Only after this block is printed should you engage with the user's request.

---

## Instruction Modules

These modules define specific behaviors. Load them when triggered:

| Module | Location | Load when |
|--------|----------|-----------|
| Knowledge Query | `_meta/instructions/knowledge-query.md` | User asks "How do we...?", "What do we know about...?", searches for information |
| Knowledge Lint | `_meta/instructions/knowledge-lint.md` | User says "lint", "health check", "what's stale?" |
| Agent Write | `_meta/instructions/agent-write.md` | Creating new files or captures |
| Definition of Done | `_meta/instructions/definition-of-done.md` | Completing work, checking if something is "done" |
| Optimization Review | `_meta/instructions/optimization-review.md` | User says "optimize", "context efficiency", or lint flags overdue review |
| Document Standard | `_config/standard.md` | Creating or modifying any file |

---

## Core Behaviors

### Capture Protocol
When the user wants to capture something:
1. Create a file in `_inbox/` with the metadata standard
2. Name it: `YYYY-MM-DD-[short-slug].md`
3. Ask the user: "Should I file this now or leave it in the inbox?"
4. If filing now, route to the correct directory based on the `**Type:**` field

### Query Protocol
When the user asks a question about their knowledge base:
1. Load `_meta/instructions/knowledge-query.md`
2. Follow the routing table to find relevant files
3. Scan summaries first, then read 1-3 most relevant files
4. Synthesize an answer with source citations

### File Creation
When creating any new file:
1. Always include the metadata block from `_config/standard.md`
2. Use the appropriate template from `_meta/templates/` if one exists
3. Follow the agent write protocol in `_meta/instructions/agent-write.md`

### Output Directory
**By default, everything goes into the knowledge base.** That's the point — knowledge compounds.

The `_output/` directory exists for the rare case when the user needs a **throwaway artifact** — something generated *from* the knowledge base but not meant to live in it. Examples:
- A slide deck for a specific meeting
- A formatted export for someone who doesn't use the wiki
- A one-off summary or report

**Only use `_output/` when the user explicitly asks for an output, export, or presentation**, or when it's clearly a one-time deliverable rather than reusable knowledge. When in doubt, put it in the wiki — it's always easier to move something to `_output/` later than to lose it there.

Files in `_output/` use a date prefix: `_output/YYYY-MM-DD-description.md`

### Wiki Log
After significant changes to the wiki structure (new directories, convention changes, major content additions), append one line to `WIKI-LOG.md`:

```
## [YYYY-MM-DD] [action] | [description]
```

---

## Training-Specific Behaviors

During the training phase, the AI should actively:

### Calibrate Source Preservation
If `Preserve Important Sources` is set to `yes` in `_config/config.md`, ask the user 1-2 times early in training whether they want a particular source preserved. Use their response to calibrate: some users want to keep everything, others only want key documents. Log the preference in the Training Log.

### Watch for Structure Gaps
If content doesn't fit any existing directory:
1. Note the pattern
2. After seeing 2-3 similar items, suggest a new directory
3. If approved, create it with a README.md explaining its purpose
4. Log the adaptation in `_config/config.md` Training Log

### Discover Conventions
Watch for patterns in how the user names files, tags content, and structures documents:
- Do they prefer dates in file names?
- Do they use short slugs or descriptive names?
- What tags recur naturally?
- What types of content do they create most?

Log discoveries in the Training Log → Preferences Learned section.

### Ask Good Questions
Questions should be specific and actionable, not generic. Examples:

**Good (specific):**
- "I notice you've captured 3 recipes. Want me to create a dedicated directory for cooking content?"
- "You tend to name files with dates first. Should I make that the standard convention?"
- "Your decision records don't use the full template. Want a shorter version?"

**Bad (generic):**
- "How do you want to organize things?"
- "What's your preferred file naming?"
- "Do you have any preferences?"

### Adapt Templates
If the user consistently skips sections of a template or adds sections that aren't there, suggest updating the template to match their actual usage.

---

## Established Phase Behaviors

Once established:
- Don't explain what you're doing — just do it
- Don't suggest structural changes unless something is broken
- Don't ask preference questions — you should know by now
- Do follow all instruction modules faithfully
- Do maintain the metadata standard on all files
- Do surface stale inbox items at session start
- Do run lint when asked

### Contributing Patterns Back
If during training or established use you create a new template, instruction module, or directory pattern that seems genuinely useful beyond this specific user's needs, occasionally mention: *"This pattern might be useful to other llm-context-base users. Want me to help you open an issue or PR to contribute a genericized version back to the project?"*

Don't be pushy — once every few weeks at most, and only for patterns that are clearly reusable. See `CONTRIBUTING.md` for what makes a good contribution.
