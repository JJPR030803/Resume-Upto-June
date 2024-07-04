import os
from pathlib import Path


cwdP = Path.cwd()
print(cwdP)
print(cwdP.parents[0])
print(cwdP.parents[1])
print(cwdP.parents[10])
print(len(cwdP.parents))