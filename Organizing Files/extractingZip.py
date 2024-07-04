import zipfile,os
from pathlib import Path

p = Path.cwd()

exampleZip  = zipfile.ZipFile(p/'example.zip')
exampleZip.extractall()


exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt',Path.cwd())
exampleZip.close()