#!/usr/bin/env python3
"""
Migrate metadata blocks from `- **Field:** value` bullet format to YAML frontmatter.

Before:
    # Title

    - **Type:** knowledge
    - **Summary:** One sentence.
    - **Tags:** #meta #standard
    - **Status:** active
    - **Updated:** 2026-04-09

    ---

    Content...

After:
    ---
    type: knowledge
    summary: One sentence.
    tags: [meta, standard]
    status: active
    updated: 2026-04-09
    ---

    # Title

    Content...
"""

import os
import re
import sys
from pathlib import Path

FIELD_ORDER = ['type', 'summary', 'tags', 'status', 'owner', 'updated', 'related', 'source']

SKIP_DIRS = {'.obsidian', '.git', 'node_modules', '_tools'}

METADATA_LINE = re.compile(r'^- \*\*(\w+):\*\* (.*)$')


def convert_tags(value):
    """'#meta #standard' -> '[meta, standard]'"""
    tags = [t.lstrip('#') for t in value.split() if t.strip()]
    return '[' + ', '.join(tags) + ']'


def yaml_value(key, value):
    if key == 'tags':
        return convert_tags(value)
    # Quote strings that contain YAML special characters
    needs_quoting = any(c in value for c in [':', '#', '[', ']', '{', '}', '*', '&', '!', '|', '>', '"', '%', '@', '`'])
    if needs_quoting:
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


def convert_file(filepath):
    text = filepath.read_text(encoding='utf-8')
    lines = text.split('\n')

    # Already has YAML frontmatter — skip
    if lines and lines[0].strip() == '---':
        return 'already-yaml'

    # Find the H1 title
    title_index = next((i for i, l in enumerate(lines) if l.startswith('# ')), None)
    if title_index is None:
        return 'no-title'

    # Skip blank lines after title to find metadata block
    i = title_index + 1
    while i < len(lines) and lines[i].strip() == '':
        i += 1

    # Must be a metadata block
    if i >= len(lines) or not METADATA_LINE.match(lines[i]):
        return 'no-metadata'

    # Parse all metadata lines
    fields = {}
    while i < len(lines):
        m = METADATA_LINE.match(lines[i])
        if m:
            fields[m.group(1).lower()] = m.group(2).strip()
            i += 1
        else:
            break

    # Skip blank lines then the --- separator
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i < len(lines) and lines[i].strip() == '---':
        i += 1

    body_lines = lines[i:]

    # Strip leading blank lines from body
    while body_lines and body_lines[0].strip() == '':
        body_lines.pop(0)

    # Build YAML frontmatter
    yaml = ['---']
    for key in FIELD_ORDER:
        if key in fields:
            yaml.append(f'{key}: {yaml_value(key, fields[key])}')
    for key, value in fields.items():
        if key not in FIELD_ORDER:
            yaml.append(f'{key}: {yaml_value(key, value)}')
    yaml.append('---')

    title_line = lines[title_index]
    new_content = '\n'.join(yaml) + '\n\n' + title_line + '\n'
    if body_lines:
        new_content += '\n' + '\n'.join(body_lines)
    if not new_content.endswith('\n'):
        new_content += '\n'

    filepath.write_text(new_content, encoding='utf-8')
    return 'converted'


def main():
    root = Path('.')
    results = {'converted': [], 'already-yaml': [], 'no-metadata': [], 'no-title': [], 'error': []}

    for md_file in sorted(root.rglob('*.md')):
        parts = set(md_file.parts[:-1])
        if parts & SKIP_DIRS or any(p.startswith('.') for p in md_file.parts[:-1]):
            continue

        try:
            result = convert_file(md_file)
            results[result].append(str(md_file))
        except Exception as e:
            results['error'].append(f'{md_file}: {e}')

    print(f"✓ Converted:      {len(results['converted'])} files")
    for f in results['converted']:
        print(f'    {f}')
    print(f"— Already YAML:   {len(results['already-yaml'])} files")
    print(f"— No metadata:    {len(results['no-metadata'])} files")
    for f in results['no-metadata']:
        print(f'    {f}')
    if results['error']:
        print(f"✗ Errors:         {len(results['error'])} files")
        for f in results['error']:
            print(f'    {f}')


if __name__ == '__main__':
    main()
