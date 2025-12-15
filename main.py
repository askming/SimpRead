import os
import glob
import subprocess
import datetime
import argparse
import re

SOURCE = './Saved_Reading'

def extract_saved_date(file_path):
    """Extract saved_date and title from file metadata:
    - For .md files: check YAML front matter for saved_date and title
    - For .epub files: check meta tag in XHTML for saved_date
    - For .pdf files: fall back to git log
    
    Returns dict with 'date', 'date_str', 'year', and 'title' (if available)
    """
    result = {}
    
    try:
        if file_path.endswith('.md'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1200)  # Read first part for front matter
                # Look for YAML front matter: ---\nsaved_date: ISO_DATETIME\ntitle: "..."
                date_match = re.search(r'saved_date:\s*([^\n\r]+)', content)
                title_match = re.search(r'title:\s*"?(.+?)"?\s*(?:\n|---)', content)

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

            if created_year != current_year:
                year_counters[created_year] = 0
                f.write(f"## {created_year}\n\n")
                f.write(f"_{file_years_count[created_year]} articles_\n\n")
                current_year = created_year        
            
            year_counters[created_year] += 1
            
            if year_counters[created_year] == 6:
                f.write("<details><summary>Show more</summary>\n\n")
            
            f.write(f"- [{display_title}]({filepath_display}), _added on {created_date}_\n\n")
            
            if year_counters[created_year] == file_years_count[current_year]:
                f.write("</details>\n\n")   

if __name__ == "__main__":
    read_list_files()
