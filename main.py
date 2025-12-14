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
                content = f.read(800)  # Read first 800 chars for front matter
                # Look for YAML front matter: ---\nsaved_date: YYYY-MM-DD\ntitle: ...
                date_match = re.search(r'---\s*\nsaved_date:\s*(\d{4}-\d{2}-\d{2})', content)
                title_match = re.search(r'title:\s*(.+?)(?:\n|---)', content)
                
                if date_match:
                    date_str = date_match.group(1)
                    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    result = {
                        'date': date,
                        'date_str': str(date),
                        'year': str(date.year)
                    }
                    if title_match:
                        result['title'] = title_match.group(1).strip()
                    
                    if date_match:  # If we found saved_date, return it
                        return result
        
        elif file_path.endswith('.epub'):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(1000)  # Read first 1000 chars for meta tag
                # Look for meta tag: <meta name="saved_date" content="YYYY-MM-DD"/>
                match = re.search(r'<meta\s+name="saved_date"\s+content="(\d{4}-\d{2}-\d{2})"', content)
                if match:
                    date_str = match.group(1)
                    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    return {
                        'date': date,
                        'date_str': str(date),
                        'year': str(date.year)
                    }
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
            # Parse ISO format: 2025-12-14T10:30:45+00:00
            date = datetime.datetime.fromisoformat(date_str).date()
            return {
                'date': date,
                'date_str': str(date),
                'year': str(date.year)
            }
    except (subprocess.TimeoutExpired, Exception):
        pass
    
    # Fallback: use current date if git log fails
    today = datetime.date.today()
    return {
        'date': today,
        'date_str': str(today),
        'year': str(today.year)
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
    
    # Sort by date using cached metadata
    filepaths.sort(key=lambda path: file_metadata[path]['date'], reverse=True)
    
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
            created_date = metadata['date_str']
            created_year = metadata['year']
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
