import os
import glob
import subprocess
import datetime
import argparse

SOURCE = './Saved_Reading'

def get_file_metadata(file_path):
    """Get file creation date using local git history (no API calls)"""
    try:
        # Get the commit that first added this file (creation date)
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", file_path],
            capture_output=True, text=True, timeout=5
        )
        
        if result.returncode == 0 and result.stdout:
            # Take the last (oldest) commit that added the file
            date_str = result.stdout.strip().split('\n')[-1]
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
    
    # Cache metadata for all files in a single pass (using local git, no API calls)
    file_metadata = {}
    for path in filepaths:
        file_metadata[path] = get_file_metadata(path)
    
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

            if created_year != current_year:
                year_counters[created_year] = 0
                f.write(f"## {created_year}\n\n")
                f.write(f"_{file_years_count[created_year]} articles_\n\n")
                current_year = created_year        
            
            year_counters[created_year] += 1
            
            if year_counters[created_year] == 6:
                f.write("<details><summary>Show more</summary>\n\n")
            
            f.write(f"- [{filename}]({filepath_display}), _added on {created_date}_\n\n")
            
            if year_counters[created_year] == file_years_count[current_year]:
                f.write("</details>\n\n")   

if __name__ == "__main__":
    read_list_files()
