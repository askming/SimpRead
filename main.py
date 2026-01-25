import os
import glob
import subprocess
import datetime
import argparse
import re
import time
try:
    from google import genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

SOURCE = './Saved_Reading'

# Fallback keywords
TAG_KEYWORDS = {
    "Technology": ["python", "programming", "software", "developer", "web dev", "linux", "artificial intelligence", "chatgpt", "llm", "machine learning", "neural network", "algorithm", "database", "cybersecurity", "frontend", "backend", "api", "framework", "git", "github"],
    "Finance": ["investment", "stock market", "economy", "capital", "wealth", "tax", "trading", "crypto", "bitcoin", "etf", "interest rate", "inflation", "recession", "bank", "financial"],
    "Productivity": ["productivity", "habit", "time management", "focus", "procrastination", "career", "learning", "memory", "deep work", "workflow", "decision making"],
    "Health": ["health", "sleep", "exercise", "diet", "nutrition", "medicine", "mental health", "stress", "disease", "covid", "virus", "neuroscience", "dopamine", "brain"],
    "Science": ["science", "physics", "mathematics", "biology", "astronomy", "universe", "energy", "climate change", "research", "scientific", "chemistry"],
    "Society": ["culture", "history", "politics", "sociology", "philosophy", "demographics", "policy", "government", "democracy", "civilization", "urban planning"],
}

def generate_tags_keyword(content, title):
    """Generate tags based on keywords in content and title, ranked by relevance (weighted score)"""
    tag_scores = {}
    title_lower = title.lower()
    content_lower = content.lower()
    
    for tag, keywords in TAG_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            # Title matches are worth 5 points
            if keyword in title_lower:
                 score += 5
            # Content matches are worth 1 point per occurrence
            score += content_lower.count(keyword)
        
        if score >= 2:
            tag_scores[tag] = score
    
    sorted_tags = sorted(tag_scores.items(), key=lambda item: item[1], reverse=True)
    return [tag for tag, score in sorted_tags]

def generate_tags_llm(content, title):
    """Generate tags using Gemini API"""
    if not HAS_GENAI:
        return None
        
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None

    try:
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
        Analyze the full text of the article below.
        Classify it into EXACTLY ONE of these categories:
        - Technology (Software, AI, Engineering, Tools)
        - Finance (Investing, Economics, Markets, Money)
        - Productivity (Work, Habits, Career, Learning)
        - Health (Medicine, Fitness, Psychology, Neuroscience)
        - Science (Physics, Biology, Astronomy, Research)
        - Society (Politics, History, Culture, Urbanism)

        If it fits multiple, choose the PRIMARY domain.
        Return ONLY the category name.
        
        Title: {title}
        Content:
        {content}
        """
        
        # Simple Retry Mechanism (1 retry)
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash', 
                contents=prompt
            )
        except Exception as e:
            if "429" in str(e) or "ResourceExhausted" in str(e):
                print("Rate limit hit (429). Sleeping for 60s...")
                time.sleep(60)
                response = client.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=prompt
                )
            else:
                raise e

        tag = response.text.strip()
        
        valid_tags = ["Technology", "Finance", "Productivity", "Health", "Science", "Society"]
        for v_tag in valid_tags:
            if v_tag.lower() in tag.lower():
                return [v_tag]
                
        return None
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return None

def update_file_tags(file_path, force=False):
    """Check for tags in frontmatter, generate if missing, and update file."""
    if not file_path.endswith('.md'):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if frontmatter exists
        match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        
        if match:
            frontmatter = match.group(1)
            # Check if tags already exist
            if 'tags:' in frontmatter and not force:
                 # Extract existing tags
                tag_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
                if tag_match:
                    print(f"Skipping {file_path}: Tags already present.")
                    return [t.strip().strip("'").strip('"') for t in tag_match.group(1).split(',') if t.strip()]
                print(f"Skipping {file_path}: 'tags:' field present but empty/unparseable.")
                return [] 
            
            if force:
                print(f"Force updating tags for {file_path}...")
            else:
                print(f"Generating tags for {file_path}...")

            # Generate tags
            title_match = re.search(r'title:\s*"?(.+?)"?\s*\n', frontmatter)
            title = title_match.group(1) if title_match else ""
            
            body = content[match.end():]
            
            # Try LLM first
            generated_tags = generate_tags_llm(body, title)
            
            # Fallback to keyword if LLM failed or not configured
            if not generated_tags:
                generated_tags = generate_tags_keyword(body[:4000], title) 
            # If used LLM, maybe sleep briefly to respect rate limits if processing many files
            elif os.environ.get("GEMINI_API_KEY"):
                time.sleep(4)  # Increased from 2s to 4s to fit 15 RPM 
            
            if generated_tags:
                # Remove existing tags line if forcing update
                if 'tags:' in frontmatter:
                    frontmatter = re.sub(r'tags:.*?\n', '', frontmatter).strip()

                # Insert tags into frontmatter
                tags_line = f"tags: [{', '.join(generated_tags)}]"
                new_frontmatter = frontmatter.rstrip() + "\n" + tags_line + "\n"
                new_content = content.replace(f"---\n{match.group(1)}\n---", f"---\n{new_frontmatter}---")
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return generated_tags
                
        else:
             pass
             
    except Exception as e:
        print(f"Error processing tags for {file_path}: {e}")
        
    return []

def extract_saved_date(file_path, force_update=False):
    """Extract metadata. Prefer Git Creation Date to ensure correct ordering."""
    result = {}
    
    # Always get Git metadata first to have a baseline "added date"
    git_meta = get_file_metadata_git(file_path)
    
    try:
        if file_path.endswith('.md'):
            # Ensure tags are generated (this might update modification time, so we trust git_meta for creation)
            tags = update_file_tags(file_path, force=force_update)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1500)
                title_match = re.search(r'title:\s*"?(.+?)"?\s*(?:\n|---)', content)
                tags_match = re.search(r'tags:\s*\[(.*?)\]', content)

                # Prioritize Git Creation Date if available
                if git_meta and git_meta.get('datetime'):
                    result = git_meta.copy()
                else:
                    # Fallback to current time if git fails (shouldn't happen in repo)
                    now = datetime.datetime.now()
                    result = {'datetime': now, 'date_str': now.isoformat(), 'year': str(now.year)}

                if title_match:
                    result['title'] = title_match.group(1).strip()
                
                if tags:
                     result['tags'] = tags
                elif tags_match:
                     result['tags'] = [t.strip().strip("'").strip('"') for t in tags_match.group(1).split(',') if t.strip()]

                return result
        
        elif file_path.endswith('.epub'):
             # ... (Keep existing EPUB logic or default to git) ...
             # For simplicity, let's use git for EPUB as well to be consistent on "added date"
             if git_meta:
                 return git_meta
             pass
    except (FileNotFoundError, Exception):
        pass
    
    return git_meta

def get_file_metadata_git(file_path):
    """Get file creation date from git history"""
    try:
        # --diff-filter=A finds the commit that ADDED the file (Creation Date)
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "-1", "--", file_path],
            capture_output=True, text=True, timeout=5
        )
        
        if result.returncode == 0 and result.stdout:
            date_str = result.stdout.strip()
            try:
                dt = datetime.datetime.fromisoformat(date_str)
                return {
                    'datetime': dt,
                    'date_str': dt.isoformat(),
                    'year': str(dt.year)
                }
            except ValueError:
                pass
        
        # If diff-filter=A fails (e.g. initial commit oddities), try getting the oldest commit
        result_reverse = subprocess.run(
            ["git", "log", "--reverse", "--format=%aI", "--", file_path],
            capture_output=True, text=True, timeout=5
        )
        if result_reverse.returncode == 0 and result_reverse.stdout:
            # First line is the oldest commit
            date_str = result_reverse.stdout.splitlines()[0].strip()
            try:
                dt = datetime.datetime.fromisoformat(date_str)
                return {
                    'datetime': dt,
                    'date_str': dt.isoformat(),
                    'year': str(dt.year)
                }
            except ValueError:
                pass

    except (subprocess.TimeoutExpired, Exception):
        pass
    
    # Final Fallback: use current time
    now = datetime.datetime.now()
    return {
        'datetime': now,
        'date_str': now.isoformat(),
        'year': str(now.year)
    }

def read_list_files(sourcepath=SOURCE, md_name ="./README.md", force_update=False):
    file_types = ["*.md", "*.pdf", "*.epub"]
    filepaths = []
    for ext in file_types:
        source_dir = os.path.join(sourcepath, ext)
        filepaths = filepaths + glob.glob(source_dir)
    
    # Cache metadata for all files in a single pass
    # For .md and .epub files: check for saved_date metadata first
    # For .pdf files and files without metadata: fall back to git log
    file_metadata = {}
    for path in filepaths:
        if path.endswith('.md') or path.endswith('.epub'):
            file_metadata[path] = extract_saved_date(path, force_update=force_update)
        else:
            # .pdf and other formats: use git log
            file_metadata[path] = get_file_metadata_git(path)
    
    # Sort by exact datetime using cached metadata (newest first)
    filepaths.sort(key=lambda path: file_metadata[path].get('datetime', datetime.datetime.min), reverse=True)
    
    # Count articles by year
    file_years = [file_metadata[p]['year'] for p in filepaths]
    file_years_count = dict(zip(file_years, [file_years.count(y) for y in file_years]))

    with open(md_name, "w") as f:
        current_year = ''
        f.write(f"# Saved readings\n\n")
        f.write(f"_Last updated on {str(datetime.date.today())}; Total {len(filepaths)} articles._\n\n")   
        
        year_counters = {}  # Track count per year
        
        for filepath in filepaths:
            filepath_display = filepath.replace(" ", "%20")
            filename = filepath.split('/')[-1].split('.')[0]
            metadata = file_metadata[filepath]
            # Prefer datetime object when available; display only the date part (YYYY-MM-DD)
            dt = metadata.get('datetime')
            if dt:
                created_date = dt.date().isoformat()
            else:
                date_str = metadata.get('date_str') or ''
                created_date = date_str[:10] if date_str else str(datetime.date.today())
            created_year = metadata.get('year') or created_date[:4]
            # Use original title from metadata if available, otherwise use filename
            display_title = metadata.get('title') or filename
            
            # Format tags if present - SHOW ONLY THE FIRST TAG
            tags_display = ""
            tags = metadata.get('tags')
            if tags and len(tags) > 0:
                # tags_display = f" `{'`, `'.join(tags)}`" # Option 1: code style
                tags_display = f" <sup>[{tags[0]}]</sup>" # Only show the first tag

            if created_year != current_year:
                year_counters[created_year] = 0
                f.write(f"## {created_year}\n\n")
                f.write(f"_{file_years_count[created_year]} articles_\n\n")
                current_year = created_year        
            
            year_counters[created_year] += 1
            
            if year_counters[created_year] == 6:
                f.write("<details><summary>Show more</summary>\n\n")
            
            f.write(f"- [{display_title}]({filepath_display}),{tags_display} _added on {created_date}_\n\n")
            
            if year_counters[created_year] == file_years_count[current_year]:
                f.write("</details>\n\n")   

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='Force regenerate all tags')
    args = parser.parse_args()
    
    read_list_files(force_update=args.force)

