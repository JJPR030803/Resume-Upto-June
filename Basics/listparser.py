
lista_prueba = ['hola','como','estas','soy','tu','padre']
def parse_lista(lista):
    texto = ''
    for i in range(len(lista)):
        if i == 0:
            texto = texto + str(lista[i])
        elif i == len(lista)-1:
            texto = texto + 'and ' + str(lista[i])
        else:
            texto = texto + ','+ str(lista[i])
    return texto

print(parse_lista(lista_prueba))