import os,zipfile
from pathlib import Path

p = Path.cwd()

examplezip = zipfile.ZipFile(p/'new.zip')
print(examplezip.namelist())


spaminfo = examplezip.getinfo('spam.txt')
print(spaminfo.file_size)
print(spaminfo.compress_size)
print(spaminfo.compress_type)