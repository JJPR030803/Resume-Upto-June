from pathlib import Path
import os
p = Path('spam.txt')
#p.write_text('hello world!')
#print(p.read_text())

helloFile = open(Path.cwd()/'hola.txt','r')
sonnetfile = open(Path.cwd()/'sonnet29.txt','r')

print(sonnetfile.readlines())

print(helloFile.read())