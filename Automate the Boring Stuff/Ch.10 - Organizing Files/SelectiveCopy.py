from pathlib import Path
import os, zipfile, shutil

# Walks through a folder tree
p = Path('C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Automate the Boring Stuff\\Ch.10 - Organizing Files')
for foldername, subfolders, filenames in os.walk(p):
    # Searches files with a certain extension
    for filename in filenames:
        if filename.endswith('.zip'):
            print(filename)
            # Copy these files to a new location
            shutil.copy(p/filename, Path.cwd())
