import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "DL_Project_1"

list_of_files = [
    ".github/workflows/.gitkeep", #for using github action
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath) #create accurate file name
    filedir, filename = os.path.split(filepath) #differentiate filedir and filename

    #When filedir do not exists >> Create a directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #If the target directory already exists, raise an OSError if exist_ok = False.
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    #When filepath do not exist or filepath size is 0 >> Create the mentioned file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #Creating an empty file only
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")
