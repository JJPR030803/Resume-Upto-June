import shelve


shelffile = shelve.open('mydata')
print(type(shelffile))
print(shelffile['cats'])
Gatos = list(shelffile.keys())
listaGatos = list(shelffile.values())
print(f'{Gatos[0]}:{listaGatos[0][0]}')
shelffile.close()