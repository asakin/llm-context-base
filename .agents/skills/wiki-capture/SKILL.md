---
name: wiki-capture
description: Capture new material into an llm-context-base wiki and file the inbox. Use when the user says "capture this", "add to inbox", "park this idea", throws an off-the-cuff idea, shares a web clip or document to keep, or asks to triage, file or clean up the inbox.
---

# Capture and filing

Read `.agents/wiki/config.md` first for the inbox path, structure, link style, naming and private folders. Templates for each note type are in `.agents/wiki/templates/`.

## Capture

1. Create `<inbox>/YYYY-MM-DD-short-slug.md` with frontmatter (`status: draft`, an informative `summary`, never "Auto-generated note"). Use `inbox-capture.md` as the shape.
2. If another agent or automation is writing, set `source:` to its name so triage can filter it.
3. Ask once: "File this now or leave it in the inbox?" If the user named a destination, write there directly.

**Idea throw.** When the user tosses an idea without time to discuss it: give a short first take, then park the idea in the inbox with your take and any open threads in the file. "Just park this" means park it raw, no commentary.

**Web clip.** A note tagged `clipped` (from Obsidian Web Clipper, using this repo's `assets/clipper-template.json`) carries a "Why I saved this" line. Act on it:

| Intent | Do |
|---|---|
| Read later | Leave it in the inbox; surface it at the next triage |
| Save the knowledge | Extract the key points into a note in the right folder; discard the raw clip |
| Relates to a project | File it under or link it from that project, with a line on why it matters |
| Source for a draft | Pull the relevant quotes into the draft; keep the original only if `preserve_sources` is true |
| Blank | Ask "What do you want to do with this clip?" before anything else |

Never file a raw clip as-is. Rewrite the `summary` to describe what you extracted, not the article title.

## Filing the inbox

For each item, oldest first:

1. Read it and decide what it is. Extract the durable claims, decisions, corrections and source references. Raw captures are input, not truth.
2. Look for an existing note on the same subject (search titles, `summary` fields, tags). Update it rather than creating a duplicate.
3. Otherwise create a note in the folder the Structure table in config points to, using the matching template. If nothing fits, propose a folder (and add it to Structure on approval) or leave the item in the inbox with a clear next action.
4. Set frontmatter: correct `type`, `status: draft` until the user has reviewed it, `updated` to today, two to five tags from the vocabulary already in use.
5. Link the note to the one to three notes it most relates to, in the configured link style.
6. If `preserve_sources` is true and the original is worth keeping (a key reference, a page that may disappear, something worth re-processing later), move it to `sources/YYYY-MM-DD-slug.md`. Otherwise delete the inbox file once its content is filed.
7. Keep contradictions and corrections visible: note the before and after instead of smoothing them over. Leave items that are too fresh or ambiguous in the inbox with a next action.

Never write into a `private` folder without asking. Append one `file` line to the log for a filing pass, not one per item.

## When a note is done

A note stays `draft` until it is findable and usable: content complete, frontmatter filled in, filed out of the inbox, linked to related notes. Then propose `status: active` (or `complete` for decisions, projects and todos). A decision is done when the choice, the options considered and the rationale are written down. Meeting notes are done when action items have owners. Nudge toward completion ("This looks ready. Mark it active?") instead of letting drafts pile up.
