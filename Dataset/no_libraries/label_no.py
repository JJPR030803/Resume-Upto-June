listasi = ["si" for i in range(10)]
listano = ["no" for i in range(10)]

lista = [item for pair in zip(listasi,listano)for item in pair]




def ordinal_encoding(lista):
    ordinal_list = []
    valores_unicos = list(set(lista))
    for element in lista:
        for indice,valor in enumerate(valores_unicos):
            if element == valor:
                ordinal_list.append(indice)
    return ordinal_list



print(ordinal_encoding(lista))
                

        
            
    