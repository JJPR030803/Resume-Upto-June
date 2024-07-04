from pathlib import Path
import os
currentCWD = Path.cwd()
home = Path.home()
os.chdir(currentCWD)
newPath = Path(home,'Documents\\Documentos\\Visual Studio 2022\\Python\\2023\\Automate the boring stuff\\Projects')
os.chdir(newPath)
print(Path.cwd())
#print(Path('spam')/'bacon'/'eggs')