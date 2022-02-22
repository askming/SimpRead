import os
import glob
from github import Github
import datetime

SOURCE = './Saved_Reading'

def read_list_files(sourcepath, md_name ="./README.md"):
    g = Github()
    repo = g.get_repo('askming/SimpRead')
    source_dir = os.path.join(sourcepath, '*.md')
    filepaths = glob.glob(source_dir)
    filepaths.sort(key=os.path.getmtime) # sort file by creation date

    with open(md_name, "w") as f:
        current_year = ''
        f.write(f"# Saved readings from SimpRead\n\n")
        f.write(f"_last updated on {str(datetime.date.today())}; total {len(filepaths)} articles_\n\n")   
        for i in range(len(filepaths)):  
            filepath_i = filepaths[i].replace(" ", "%20")
            filename = filepaths[i].split('/')[-1].split('.')[0]
            commits = repo.get_commits(path=filepaths[i])
            created_date = str(commits[0].commit.committer.date)[:9]
            created_year = str(commits[0].commit.committer.date)[:3]

            if created_year != current_year:
                f.write(f"## {created_date.year}\n\n")
                current_year = created_date.year
            f.write(f"- [{filename}]({filepath_i}), _added on {created_date}_\n\n")

if __name__ == "__main__":
    read_list_files(sourcepath=SOURCE)