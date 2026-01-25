Tagging tools

Quick usage:

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Dry-run suggestions:

```bash
python scripts/tag_suggester.py --dry-run
```

3. Apply suggested tags (writes YAML frontmatter to files):

```bash
python scripts/tag_suggester.py --apply
```

Notes:
- If `OPENAI_API_KEY` is set, the script will use OpenAI embeddings.
- Otherwise it will try `sentence-transformers` local model and fall back to keyword matching.
