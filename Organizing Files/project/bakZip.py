import os,zipfile
from pathlib import Path

def backup(path,nombreZip,newPath):
    folder = os.path.abspath(path)
    if newPath:
        os.chdir(newPath)
        
    with zipfile.ZipFile(nombreZip,'w',zipfile.ZIP_DEFLATED) as newZip:
        for folderName,subfolders,filenames in os.walk(folder):
            for filename in filenames:
                filePath = os.path.join(folderName,filename)
                newZip.write(filePath,compress_type=zipfile.ZIP_DEFLATED)
        