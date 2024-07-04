import re
from pathlib import Path
import os
import glob
reg = input("Que palabra quieres buscar?")
regex = re.compile(rf'\b{reg}\b')

path = Path.cwd()

archivosTexto = list(path.glob('*.txt'))

for archivo in archivosTexto:
    with open(file=archivo.absolute(),mode='r',encoding='utf-8') as a:
        content = a.read()
        match = re.search(regex,content)
        if match:
            file = os.path.basename(archivo)
            print(f'Archivo Encontrado: {file}')