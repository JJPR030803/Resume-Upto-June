import os
from pathlib import Path

p = Path.cwd()
lista = list(p.glob('*'))
archivosTexto = list(p.glob('*.txt'))
archivosF = list(p.glob('f?.py'))
print(os.path.basename(archivosTexto[0]))
print(lista[1])
for f in archivosF:
    print(os.path.basename(f))