import argparse
from pathlib import Path


#add an argument parser to read the arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument('directory', type = str)
#parser.add_argument('flags', type = str)

#parse the arguments that were passed
args = parser.parse_args()

#define the directory name using the argument
directory = Path(args.directory)
#define the flags using the argument
# flags = Path(args.directory)

#check if the directory already exists
if directory.exists():
    print(f"mkdir: cannot create directory ‘{directory}’: File exists")

#check if the directory's parent folder doesn't exist
elif not directory.parent.exists():
    #check if the parent flag is raised
    # if 
    #     directory.mkdir(parents=True)
    else:
        print(f"mkdir: cannot create directory ‘{args.directory}’: No such file or directory")

#check if the parent flag is raised
elif 

#use mkdir function to make the directory
else: 
    directory.mkdir()

#test the arguments were properly parsed
print(args.directory)