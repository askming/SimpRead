import os, pathlib
import glob
import datetime

SOURCE = './Saved_Reading'

def read_list_files(sourcepath, md_name ="./README.md"):
    os.chdir(sourcepath)
    source_dir = os.path.join(sourcepath, '*.md')
    filepaths = glob.glob(source_dir)
    filepaths.sort(key=os.path.getctime) # sort file by created date

    with open(md_name, "w") as f:
        current_year = ''
        f.write(f"# Saved readings from SimpRead\n\n")
        f.write(f"_last updated on {str(datetime.date.today())}; total {len(filepaths)} articles_\n\n")   
        for i in range(len(filepaths)):  
            filepath_i = filepaths[i].replace(" ", "%20")
            filename = filepaths[i].split('/')[-1].split('.')[0]
            fname = pathlib.Path(filepaths[i].split('/')[-1])
            created_date = datetime.datetime.fromtimestamp(fname.stat().st_ctime, tz=datetime.tzinfo.tzname("US/Pacific")).date()

            if created_date.year != current_year:
                f.write(f"## {created_date.year}\n\n")
                current_year = created_date.year
            f.write(f"- [{filename}]({filepath_i}), _added on {created_date}_\n\n")

if __name__ == "__main__":
    read_list_files(sourcepath=SOURCE)