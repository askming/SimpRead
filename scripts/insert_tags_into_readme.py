#!/usr/bin/env python3
"""Post-process README.md produced by main.py and insert first tag for each article.

For lines like:
- [Title](./Saved_Reading/Some%20File.md), _added on 2026-01-25_

This script will read the target file, extract `tags` from YAML frontmatter and
rewrite the line as:
- [Title](./Saved_Reading/Some%20File.md) — tag, _added on 2026-01-25_

Only the first tag is shown. If no tag, the line is left unchanged.
"""
import re
from pathlib import Path
import yaml

ROOT = Path.cwd()
README = ROOT / 'README.md'

LINK_LINE_RE = re.compile(r'^(\s*-\s*\[([^\]]+)\]\(([^)]+)\),\s*_added on\s*([^_]+)_\s*)$')

def read_frontmatter(path: Path):
    text = path.read_text(encoding='utf-8')
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}
            except Exception:
                return {}
    return {}

def first_tag_for_link(link_target: str):
    # Normalize path (remove leading ./)
    p = link_target
    if p.startswith('./'):
        p = p[2:]
    fp = ROOT / p
    if not fp.exists():
        return None
    fm = read_frontmatter(fp)
    tags = fm.get('tags') or []
    if isinstance(tags, list) and tags:
        return str(tags[0])
    return None

def process():
    if not README.exists():
        print('README.md not found')
        return
    lines = README.read_text(encoding='utf-8').splitlines()
    out = []
    for line in lines:
        m = LINK_LINE_RE.match(line)
        if m:
            whole, title, link, date = m.groups()
            tag = first_tag_for_link(link)
            if tag:
                # Insert tag after the link
                new_line = f"- [{title}]({link}) — {tag}, _added on {date}_"
                out.append(new_line)
                continue
        out.append(line)

    README.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('Inserted tags into README')

if __name__ == '__main__':
    process()
