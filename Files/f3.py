import os
from pathlib import Path
##os.makedirs('C:\\delicious\\walnut\\waffles')
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

Path('my/relative/path')
Path.cwd()/Path('my/relative/path')

print(os.path.abspath('Projects\\Files'))
print(os.path.isabs('Projects\\Files'))