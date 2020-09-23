
from pathlib import Path
import os
p = Path.cwd()
#Walk through a folder tree
for foldername, subfolders, filename in os.walk(p):
    print(f'checking folders {foldername}...')
    for filenames in filename:
        try:
            #searches for large files, > 100MB
            size = os.path.getsize(os.path.join(foldername,filenames))
            print(size)
            if size >= 1*10**8: 
                #Print these files on the screen
                print(f'The size of {filenames} is {size}.')
        except:
            continue
