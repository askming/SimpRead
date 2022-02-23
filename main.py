import os
import glob
from github import Github
import datetime
import argparse

SOURCE = './Saved_Reading'

def login(token):
    return Github(token)

def get_repo(user: Github, repo: str):
    return user.get_repo(repo)

def date_to_sort(repo, file_path):
    commits = repo.get_commits(path=file_path)
    date = commits[0].commit.committer.date
    return(date)


def read_list_files(token, repo_name, sourcepath=SOURCE, md_name ="./README.md"):
    user = login(token)
    repo = get_repo(user, repo_name)

    source_dir = os.path.join(sourcepath, '*.md')
    filepaths = glob.glob(source_dir)
    
    filepaths.sort(key=lambda path: date_to_sort(repo=repo, file_path=path), reverse=True) # sort file by creation date

    with open(md_name, "w") as f:
        current_year = ''
        f.write(f"# Saved readings from SimpRead\n\n")
        f.write(f"_last updated on {str(datetime.date.today())}; total {len(filepaths)} articles_\n\n")   
        for i in range(len(filepaths)):  
            filepath_i = filepaths[i].replace(" ", "%20")
            filename = filepaths[i].split('/')[-1].split('.')[0]
            commits = repo.get_commits(path=filepaths[i])
            created_date = str(commits[0].commit.committer.date)[:10]
            created_year = str(commits[0].commit.committer.date)[:4]

            if created_year != current_year:
                f.write(f"## {created_year}\n\n")
                current_year = created_year
            f.write(f"- [{filename}]({filepath_i}), _added on {created_date}_\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    options = parser.parse_args()
    read_list_files(options.github_token, options.repo_name)