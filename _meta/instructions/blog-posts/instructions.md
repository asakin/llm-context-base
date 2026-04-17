---
type: instruction
summary: How to create blog posts using the standard template and publishing flow.
tags: [meta, publishing]
status: active
updated: 2026-04-12
---

# Blog Post Instructions

## Template

Use `_meta/templates/blog-post.md` for all blog posts. Copy it to the appropriate location (typically `5-Publishing/` or wherever the user's publishing folder lives) and fill in each section.

---

## Visual Plan (Required)

Every blog post must have a Visual Plan section filled out **before** writing the full draft. The plan ensures posts are scannable and engaging.

**Minimum:** 2-3 visual elements per post, chosen from:

- **Code / data blocks** — real examples, not hypothetical. Readers skim for code.
- **Tables** — comparisons, summaries, before/after. Use when prose would repeat a pattern.
- **Screenshots** — annotated where possible. Every screenshot requires:
  - **Placement** — where it goes relative to the text
  - **Alt text** — accessible description for screen readers
  - **Caption** — contextual label for sighted readers
- **Pull quotes** — highlight a key insight or provocative claim. Use sparingly.

If a post has zero visual elements, push back and ask what could be added.

---

## SEO Keywords

Keywords should be **problem-first, not product-first**.

Good: `automate deployment pipeline`, `reduce CI build time`
Bad: `MyTool features`, `MyTool deployment`

Think about what someone would search for when they have the problem your post solves. Put yourself in the reader's shoes before they know your solution exists.

Place 3-5 keywords in the frontmatter `seo_keywords` field.

---

## Publishing Flow

1. **Draft** — Write in the template. Fill out the Visual Plan first, then the Full Draft.
2. **Review** — Self-review or peer review. Check that:
   - Visual Plan elements are all present in the draft
   - Screenshots have alt text and captions
   - SEO keywords appear naturally in the text
   - The Social Post section is ready to copy-paste
3. **Publish** — Post to the primary platform. Update `status: published` and the `updated` date in frontmatter.
4. **Cross-post** — Adapt for secondary platforms (newsletter, social, etc.). Use the Social Post section as the starting point.
5. **Track** — Update the post file with the published URL and any cross-post links.

---

## Screenshot Requirements

Screenshots are not optional decoration. Every screenshot must be intentional:

- **Placement** must be specified (e.g., "after the setup section", "before the results table")
- **Alt text** must describe what the screenshot shows, not just "screenshot of the UI"
- **Caption** must give context a reader needs — what should they notice?

If a screenshot doesn't have all three, it's not ready.

---

## The P.S. Convention

If something notable happened during the writing process — an unexpected discovery, a tangent that deserves its own post, a process observation — capture it in the P.S. section at the bottom.

This is optional but encouraged. It adds a human touch and can seed future content.

---

## File Naming

Blog post files should follow the standard:
```
YYYY-MM-DD-short-description.md
```

Example: `2026-04-12-visual-planning-for-blog-posts.md`
