import os
from pathlib import Path

calcFile = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFile))
print(os.path.dirname(calcFile))
print(os.path.split(calcFile))
print(calcFile.split(os.sep))