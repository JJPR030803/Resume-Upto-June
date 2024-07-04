import csv
with open("Dataset\Online Sales Data.csv","r") as file:
    listaDatos = []
    reader = csv.reader(file)
    for row in reader:
        listaDatos.append(row)
        
        
    columnas_numericas = [columna[4:7] for columna in listaDatos[1:]]
    columna_producto_categoria = [columna[2] for columna in listaDatos[1:]]
    columna_nombre_producto = [columna[3] for columna in listaDatos[1:]]
    lista_nombres = []
    lista_categoria = []
    
    
    
for v in columna_producto_categoria:
    if v not in lista_categoria:
        lista_categoria.append(v)


for v in columna_nombre_producto:
    if v not in lista_nombres:
        lista_nombres.append(v)
        
        

        
def categorical_frequency(lista,lista_cat_total):
    lista_frequency = [0 for v in lista_cat_total]
    for i,cat in enumerate(lista_cat_total):
        contador = 0
        for value in lista:
            if value == cat:
                contador+=1
        lista_frequency[i] = contador
    #print(lista_frequency)


def one_hot(columna,valores_unicos):
    value_to_index = {value: index for index, value in enumerate(valores_unicos)}
    
    
    # Initialize the matrix with zeros
    one_hot_matrix = [[0] * len(valores_unicos) for _ in range(len(columna))]
    
    
    for row_index, value in enumerate(columna):
        column_index = value_to_index[value]
        one_hot_matrix[row_index][column_index] = 1

    return one_hot_matrix
    
sorted_lista = sorted(lista_categoria)
print(sorted_lista)
        
#categorical_frequency(lista=columna_producto_categoria,lista_cat_total=lista_categoria)
one_hot_category = one_hot(valores_unicos=sorted_lista,columna=columna_producto_categoria)
print(one_hot_category[1])
    
    
    
    
    


