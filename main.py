import os
import glob
from datetime import date

SOURCE = './Saved_Reading'

def read_list_files(sourcepath, md_name ="README.md"):

    source_dir = os.path.join(sourcepath, '*.md')
    filepaths = (glob.glob(source_dir))
    filenames = [p.split('/')[-1].split('.')[0] for p in filepaths]

    with open(md_name, "w") as f:
        f.write(f"# Saved readings from SimpRead\n\n")
        f.write(f"_last updated on " + str(date.today()) + "_\n\n")   
        for i in range(len(filepaths)):  
            f.write(f"- [{filenames[i]}]({filepaths[i]})\n\n")

if __name__ == "__main__":
    read_list_files(sourcepath=SOURCE)