import os
import shutil
import logging
from tqdm import tqdm

__author__ = "Miguel Angel Salinas Gancedo"
__copyright__ = "Simur"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

# Some configurations
SOURCE_ROOT = '/media/simur/maxone/COMPLETOS'
DESTINATION_ROOT = '/home/simur/git/uniovi-simur-wearablepermed-data'
EXCLUDED_EXTENSIONS = { '.MOV', '.JPG' } 

# First, collect all files to be copied
files_to_copy = []

def setup_loggin(loglevel):
    logformat = ""
    
for root, dirs, files in os.walk(SOURCE_ROOT):
    for file in files:
        if not any(file.endswith(ext) for ext in EXCLUDED_EXTENSIONS):
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, start=SOURCE_ROOT)
            destination_file = os.path.join(DESTINATION_ROOT, relative_path)
            files_to_copy.append((source_file, destination_file))

# Now, copy files with progress bar
with tqdm(total=len(files_to_copy), unit="file") as pbar:
    for source_file, destination_file in files_to_copy:
        pbar.set_description(f"Copying: {os.path.basename(source_file)}")
        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        shutil.copy2(source_file, destination_file)
        pbar.update(1)

print("Files copied successfully.")