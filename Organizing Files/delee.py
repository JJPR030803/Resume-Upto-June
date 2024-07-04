import os
from pathlib import Path

for filename in Path.cwd().glob('*.rxt'):
    os.unlink(filename)
    print(filename.name)