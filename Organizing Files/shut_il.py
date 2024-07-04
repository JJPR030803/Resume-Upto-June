import shutil,os
from pathlib import Path

p = Path.cwd()

shutil.copy(p/'spam.txt',p/'spam_backup')