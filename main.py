import os
import glob
from github import Github, Auth
import datetime
import argparse

SOURCE = './Saved_Reading'

def login(token):
    auth = Auth.Token(token)
    return Github(auth=auth)

def get_repo(user: Github, repo: str):
    return user.get_repo(repo)

def get_file_metadata(repo, file_path):
    """Cache commit data to avoid multiple API calls per file"""
    commits = repo.get_commits(path=file_path)
    commit = commits[0].commit.committer
    date = commit.date
    return {
        'date': date,
        'date_str': str(date)[:10],
        'year': str(date)[:4]
    }

def read_list_files(token, repo_name, sourcepath=SOURCE, md_name ="./README.md"):
    user = login(token)
    repo = get_repo(user, repo_name)

    file_types = ["*.md", "*.pdf", "*.epub"]
    filepaths = []
    for ext in file_types:
        source_dir = os.path.join(sourcepath, ext)
        filepaths = filepaths + glob.glob(source_dir)
    
    # Cache metadata for all files in a single pass
    file_metadata = {}
    for path in filepaths:
        file_metadata[path] = get_file_metadata(repo, path)
    
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
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    options = parser.parse_args()
    read_list_files(options.github_token, options.repo_name)
