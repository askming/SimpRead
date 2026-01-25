#!/usr/bin/env python3
"""Suggest tags for markdown files under Saved_Reading using embeddings or keyword fallback.

Usage:
  python scripts/tag_suggester.py --dry-run
  python scripts/tag_suggester.py --apply

Supports OpenAI embeddings if OPENAI_API_KEY is set, otherwise uses sentence_transformers if available, else falls back to keyword counts.
"""
import os
import sys
import argparse
import json
from pathlib import Path
import yaml
import re
from collections import defaultdict, Counter

try:
    import numpy as np
except Exception:
    print("numpy is required. Please install dependencies from requirements.txt")
    raise

ROOT = Path.cwd()
SAVED = ROOT / "Saved_Reading"
TAXONOMY = ROOT / "tagger" / "taxonomy.yml"
INDEX_OUT = ROOT / "tags_index.json"

def list_markdown_files(root):
    return sorted(root.rglob("*.md"))

def read_markdown(path):
    text = path.read_text(encoding='utf-8')
    # strip YAML frontmatter if present
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text

def load_taxonomy(path):
    if not path.exists():
        raise FileNotFoundError(f"taxonomy file not found: {path}")
    return yaml.safe_load(path)

def simple_keyword_scores(text, taxonomy):
    lc = text.lower()
    scores = {}
    for tag, info in taxonomy.items():
        keywords = info.get('keywords', []) + ([info.get('description', '')] if info.get('description') else [])
        count = 0
        for kw in keywords:
            if not kw: continue
            count += lc.count(kw.lower())
        scores[tag] = float(count)
    return scores

def embed_via_openai(texts):
    try:
        import openai
    except Exception:
        raise RuntimeError('openai package not installed')
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise RuntimeError('OPENAI_API_KEY not set')
    openai.api_key = key
    # batch call per item
    embs = []
    for t in texts:
        resp = openai.Embedding.create(input=t, model='text-embedding-3-small')
        embs.append(np.array(resp['data'][0]['embedding'], dtype=float))
    return np.vstack(embs)

def embed_via_sbert(texts):
    try:
        from sentence_transformers import SentenceTransformer
    except Exception:
        raise RuntimeError('sentence_transformers not available')
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return np.array(model.encode(texts, show_progress_bar=False))

def cosine_sim_matrix(A, B):
    # A: n x d, B: m x d -> n x m
    An = A / np.linalg.norm(A, axis=1, keepdims=True)
    Bn = B / np.linalg.norm(B, axis=1, keepdims=True)
    return An @ Bn.T

def suggest_tags_for_docs(doc_texts, taxonomy, top=3):
    tags = list(taxonomy.keys())
    tag_texts = [ (taxonomy[t].get('description') or '') + ' ' + ' '.join(taxonomy[t].get('keywords', [])) for t in tags ]
    embeddings_method = None
    use_openai = bool(os.environ.get('OPENAI_API_KEY'))
    try:
        if use_openai:
            doc_embs = embed_via_openai(doc_texts)
            tag_embs = embed_via_openai(tag_texts)
            embeddings_method = 'openai'
        else:
            doc_embs = embed_via_sbert(doc_texts)
            tag_embs = embed_via_sbert(tag_texts)
            embeddings_method = 'sbert'
    except Exception:
        doc_embs = None
        tag_embs = None

    results = []
    if doc_embs is not None and tag_embs is not None:
        sims = cosine_sim_matrix(doc_embs, tag_embs)
        for i in range(sims.shape[0]):
            idxs = np.argsort(-sims[i])[:top]
            res = [(tags[j], float(sims[i,j])) for j in idxs]
            results.append(res)
    else:
        # fallback keyword scoring
        for txt in doc_texts:
            scores = simple_keyword_scores(txt, taxonomy)
            best = sorted(scores.items(), key=lambda x: -x[1])[:top]
            results.append([(k, v) for k,v in best if v>0])

    return results, embeddings_method

def write_frontmatter(path, tags):
    text = path.read_text(encoding='utf-8')
    fm = {'tags': tags}
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            # merge or replace tags
            existing = yaml.safe_load(parts[1]) or {}
            existing.update(fm)
            new = '---\n' + yaml.safe_dump(existing, allow_unicode=True) + '---\n' + parts[2].lstrip('\n')
            path.write_text(new, encoding='utf-8')
            return
    new = '---\n' + yaml.safe_dump(fm, allow_unicode=True) + '---\n\n' + text
    path.write_text(new, encoding='utf-8')

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--apply', action='store_true')
    p.add_argument('--top', type=int, default=3)
    p.add_argument('--force-keyword', action='store_true', help='Force keyword-only tagging (no embeddings)')
    args = p.parse_args()

    taxonomy = load_taxonomy(TAXONOMY)
    files = list_markdown_files(SAVED)
    if not files:
        print('No markdown files found under Saved_Reading')
        return

    doc_texts = [ read_markdown(f)[:4000] for f in files ]
    if args.force_keyword:
        # Skip embeddings and use keyword fallback only
        suggestions = []
        for txt in doc_texts:
            scores = simple_keyword_scores(txt, taxonomy)
            best = sorted(scores.items(), key=lambda x: -x[1])[:args.top]
            suggestions.append([(k, v) for k, v in best if v > 0])
        method = 'keyword'
    else:
        suggestions, method = suggest_tags_for_docs(doc_texts, taxonomy, top=args.top)

    index = defaultdict(list)
    for f, sug in zip(files, suggestions):
        tag_names = [ t for t,_ in sug ]
        print(f"{f.relative_to(ROOT)} -> {tag_names}  (method={method})")
        for t in tag_names:
            index[t].append(str(f.relative_to(ROOT)))
        if args.apply and tag_names:
            write_frontmatter(f, tag_names)

    with open(INDEX_OUT, 'w', encoding='utf-8') as fh:
        json.dump(index, fh, indent=2, ensure_ascii=False)

    print(f"Wrote index to {INDEX_OUT}")

if __name__ == '__main__':
    main()
