#!/usr/bin/env python3
"""Convert llm-context-base v1 bold-field metadata to YAML frontmatter.

Handles both v1 shapes, each either directly under the `# Title` or at the very top
of a file with no title (Web Clipper notes):

    - **Type:** knowledge        (v1.1 bullets)
    **Type:** knowledge          (v1.0 lines)

Usage:
    migrate-frontmatter.py [ROOT] [--dry-run]    convert every .md under ROOT (default .)
    migrate-frontmatter.py --self-test           run the built-in checks
"""

import re
import sys
import tempfile
from pathlib import Path

FIELD_ORDER = ['type', 'summary', 'tags', 'status', 'owner', 'updated', 'related', 'source']
SKIP_DIRS = {'.obsidian', '.git', '.agents', '.claude', 'node_modules', '_tools'}
METADATA_LINE = re.compile(r'^(?:- )?\*\*(\w+):\*\*\s?(.*)$')
YAML_SPECIAL = set(':#[]{}*&!|>"%@`')


def main(argv):
    if '--self-test' in argv:
        self_test()
        print('self-test passed')
        return 0
    dry_run = '--dry-run' in argv
    paths = [a for a in argv if not a.startswith('--')]
    root = Path(paths[0] if paths else '.')
    results = {'converted': [], 'already-yaml': [], 'no-metadata': [], 'error': []}

    for md_file in sorted(root.rglob('*.md')):
        if set(md_file.relative_to(root).parts[:-1]) & SKIP_DIRS:
            continue
        try:
            results[convert_file(md_file, dry_run)].append(str(md_file))
        except (OSError, UnicodeDecodeError) as e:
            results['error'].append(f'{md_file}: {e}')

    verb = 'Would convert' if dry_run else 'Converted'
    print(f"{verb}: {len(results['converted'])} files")
    for f in results['converted']:
        print(f'    {f}')
    print(f"Already YAML: {len(results['already-yaml'])} files")
    print(f"No v1 metadata: {len(results['no-metadata'])} files")
    for f in results['error']:
        print(f'Error: {f}')
    return 1 if results['error'] else 0


def convert_file(filepath, dry_run=False):
    new_content = convert_text(filepath.read_text(encoding='utf-8'))
    if new_content in ('already-yaml', 'no-metadata'):
        return new_content
    if not dry_run:
        filepath.write_text(new_content, encoding='utf-8')
    return 'converted'


def convert_text(text):
    lines = text.split('\n')
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    if first is None:
        return 'no-metadata'
    if lines[first].strip() == '---':
        return 'already-yaml'

    # Only the first non-blank line can be the title, so a '# ' inside a code block never counts.
    title = lines[first] if lines[first].startswith('# ') else None
    i = first + 1 if title else first
    while title and i < len(lines) and not lines[i].strip():
        i += 1

    fields = {}
    while i < len(lines) and (m := METADATA_LINE.match(lines[i])):
        fields[m.group(1).lower()] = m.group(2).strip()
        i += 1
    if not fields:
        return 'no-metadata'

    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip() == '---':
        i += 1
    body = lines[i:]
    while body and not body[0].strip():
        body.pop(0)

    keys = [k for k in FIELD_ORDER if k in fields] + [k for k in fields if k not in FIELD_ORDER]
    out = ['---'] + [f'{k}: {yaml_value(k, fields[k])}' for k in keys] + ['---', '']
    if title:
        out += [title, '']
    out += body
    result = '\n'.join(out)
    return result if result.endswith('\n') else result + '\n'


def yaml_value(key, value):
    if key == 'tags':
        return '[' + ', '.join(t.lstrip('#') for t in value.split()) + ']'
    if any(c in YAML_SPECIAL for c in value):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return value


def self_test():
    bullets = '# T\n\n- **Type:** knowledge\n- **Tags:** #a #b\n- **Updated:** 2026-04-09\n\n---\n\nBody\n'
    assert convert_text(bullets) == '---\ntype: knowledge\ntags: [a, b]\nupdated: 2026-04-09\n---\n\n# T\n\nBody\n'
    lines_v10 = '# T\n\n**Type:** decision\n**Summary:** Chose X: cheaper\n\n---\n\nBody\n'
    assert convert_text(lines_v10) == '---\ntype: decision\nsummary: "Chose X: cheaper"\n---\n\n# T\n\nBody\n'
    clip = '**Type:** knowledge\n**Tags:** #clipped\n\n---\n\n> Why I saved this: x\n'
    assert convert_text(clip) == '---\ntype: knowledge\ntags: [clipped]\n---\n\n> Why I saved this: x\n'
    assert convert_text('---\ntype: x\n---\n# T\n') == 'already-yaml'
    assert convert_text('Intro\n\n```\n# not a title\n**Type:** x\n```\n') == 'no-metadata'
    assert convert_text('') == 'no-metadata'
    with tempfile.TemporaryDirectory() as d:
        note = Path(d, 'n.md')
        note.write_text(bullets, encoding='utf-8')
        assert convert_file(note, dry_run=True) == 'converted' and note.read_text(encoding='utf-8') == bullets


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
