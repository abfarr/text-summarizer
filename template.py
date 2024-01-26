import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "testSummarizer" # src

# List of files for a general template
list_of_files = [
    ".github/workflows/.gitkeep",  # .github - for CI/CD library; .gitkeep - track empty files
    f"src/{project_name}/__init__.py",  # all __init__.py = constructor files
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",  # configurations
    "params.yaml",  # config params    
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)# handle path issues by OS
    filedir, filename = os.path.split(filepath)

    # Check if there's a directory listed (ie, not a standalone file)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create files if they do not yet exist (or is empty)
    if (not os.path.exists(filepath)) or  (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f"Creating empty file: {filepath}")
            pass
    else:
        logging.info(f"File {filepath} already exists")