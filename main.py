import os
import glob
import subprocess
import datetime
import argparse
import re
import time
try:
    import google.generativeai as genai
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
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-latest') # Use a fast/cheap model
        
        prompt = f"""
        Analyze the following article content and title. 
        Identify the single most relevant category from this list: [Technology, Finance, Productivity, Health, Science, Society]. 
        Return ONLY the category name. If none fit perfectly, choose the closest one.
        
        Title: {title}
        Content Snippet:
        {content[:4000]}
        """
        
        response = model.generate_content(prompt)
        tag = response.text.strip()
        
        # Validate response is in our list
        valid_tags = ["Technology", "Finance", "Productivity", "Health", "Science", "Society"]
        # Basic cleanup
        for v_tag in valid_tags:
            if v_tag.lower() in tag.lower():
                return [v_tag]
                
        return None
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return None

def update_file_tags(file_path):
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
            if 'tags:' in frontmatter:
                 # Extract existing tags
                tag_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
                if tag_match:
                    print(f"Skipping {file_path}: Tags already present.")
                    return [t.strip().strip("'").strip('"') for t in tag_match.group(1).split(',') if t.strip()]
                print(f"Skipping {file_path}: 'tags:' field present but empty/unparseable.")
                return [] 
            
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
                time.sleep(4) # Free tier has roughly 15 RPM = 4 sec/req
            
            if generated_tags:
                # Insert tags into frontmatter
                tags_line = f"tags: [{', '.join(generated_tags)}]"
                new_frontmatter = frontmatter.rstrip() + "\n" + tags_line + "\n"
                new_content = content.replace(f"---\n{frontmatter}\n---", f"---\n{new_frontmatter}---")
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return generated_tags
                
        else:
             pass
             
    except Exception as e:
        print(f"Error processing tags for {file_path}: {e}")
        
    return []

def extract_saved_date(file_path):
    """Extract saved_date, title, and tags from file metadata:
    - For .md files: check YAML front matter for saved_date, title, and tags
    - For .epub files: check meta tag in XHTML for saved_date
    - For .pdf files: fall back to git log
    
    Returns dict with 'date', 'date_str', 'year', 'title', and 'tags' (if available)
    """
    result = {}
    
    try:
        if file_path.endswith('.md'):
            # First, ensure tags are up to date/generated
            tags = update_file_tags(file_path)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1500)  # Read first part for front matter
                # Look for YAML front matter: ---\nsaved_date: ISO_DATETIME\ntitle: "..."
                date_match = re.search(r'saved_date:\s*([^\n\r]+)', content)
                title_match = re.search(r'title:\s*"?(.+?)"?\s*(?:\n|---)', content)
                tags_match = re.search(r'tags:\s*\[(.*?)\]', content)

                if date_match:
                    date_str_raw = date_match.group(1).strip()
                    try:
                        dt = datetime.datetime.fromisoformat(date_str_raw)
                    except Exception:
                        # Fallback: if only a date is present, parse as date at midnight
                        try:
                            d = datetime.datetime.strptime(date_str_raw, '%Y-%m-%d').date()
                            dt = datetime.datetime.combine(d, datetime.time.min)
                        except Exception:
                            dt = None

                    if dt:
                        result = {
                            'datetime': dt,
                            'date_str': dt.isoformat(),
                            'year': str(dt.year)
                        }
                        if title_match:
                            result['title'] = title_match.group(1).strip()
                        
                        # Use tags from processing or regex
                        if tags:
                             result['tags'] = tags
                        elif tags_match:
                             result['tags'] = [t.strip().strip("'").strip('"') for t in tags_match.group(1).split(',') if t.strip()]

                        return result
        
        elif file_path.endswith('.epub'):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(1200)  # Read first part for meta tag
                # Look for meta tag: <meta name="saved_date" content="ISO_DATETIME"/>
                match = re.search(r'<meta\s+name="saved_date"\s+content="([^"]+)"', content)
                if match:
                    date_str_raw = match.group(1).strip()
                    try:
                        dt = datetime.datetime.fromisoformat(date_str_raw)
                        return {
                            'datetime': dt,
                            'date_str': dt.isoformat(),
                            'year': str(dt.year)
                        }
                    except Exception:
                        try:
                            d = datetime.datetime.strptime(date_str_raw, '%Y-%m-%d').date()
                            dt = datetime.datetime.combine(d, datetime.time.min)
                            return {
                                'datetime': dt,
                                'date_str': dt.isoformat(),
                                'year': str(dt.year)
                            }
                        except Exception:
                            pass
    except (FileNotFoundError, Exception):
        pass
    
    # Fallback: use git log if no metadata found
    return get_file_metadata_git(file_path)

def get_file_metadata_git(file_path):
    """Get file date from git history using the last commit that modified it"""
    try:
        # Use the last commit that touched this file (most recent modification, not just creation)
        # This better preserves the actual save date
        result = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "--", file_path],
            capture_output=True, text=True, timeout=5
        )
        
        if result.returncode == 0 and result.stdout:
            date_str = result.stdout.strip()
            # Parse ISO format into datetime (may include timezone)
            try:
                dt = datetime.datetime.fromisoformat(date_str)
            except Exception:
                # Fallback: parse as date only
                try:
                    d = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    dt = datetime.datetime.combine(d, datetime.time.min)
                except Exception:
                    dt = None

            if dt:
                return {
                    'datetime': dt,
                    'date_str': dt.isoformat(),
                    'year': str(dt.year)
                }
    except (subprocess.TimeoutExpired, Exception):
        pass
    
    # Fallback: use current datetime if git log fails
    now = datetime.datetime.now()
    return {
        'datetime': now,
        'date_str': now.isoformat(),
        'year': str(now.year)
    }

def read_list_files(sourcepath=SOURCE, md_name ="./README.md"):
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
            file_metadata[path] = extract_saved_date(path)
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
    read_list_files()

