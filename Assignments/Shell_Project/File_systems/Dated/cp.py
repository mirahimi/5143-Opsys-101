import argparse
import shutil
from pathlib import Path

    # more info on shutil https://docs.python.org/3/library/shutil.html 

    # add an argument parser to read the arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument('source', type=str)
parser.add_argument('destination', type=str)

    # parse the arguments that were passed
args = parser.parse_args()

    # define the source and destinations using the parsed arguments
source_path = Path(args.source)
destination_path = Path(args.destination)

    # Check if the source doesn't exist
if not source_path.exists():
    print(f"cp: cannot stat '{args.source}': No such file or directory")

    # Otherwise copy the source to the destination
else:
    shutil.copy(str(source_path), str(destination_path))
    print(f"Copied '{args.source}' to '{args.destination}'")