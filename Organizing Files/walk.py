import os
from pathlib import Path

for foldername,subfolders, filenames in os.walk(Path.cwd()/'delicious'):
    print('The current folder is'+foldername)
    
    for subfolder in subfolders:
        print('SUBFOLDERS OF:'+foldername)
        
    for filename in filenames:
        print('FILE INSIDE'+':'+filename)
    print('')