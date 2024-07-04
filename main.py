import numbers as np
import csv
import matplotlib.pyplot as plt
def convertint(fila11):
    for i in range(len(fila11)):
        if fila11[i] == 'conventional':
            fila11[i] = 0
        elif fila11[i] == 'organic':
            fila11[i] = 1
def convertTypes(valor):
    if valor == 'conventional':
        valor = 1
    elif valor == 'organic':
        valor = 2
    else:
        valor = 3
    return valor
def extract(dataset,index):
    for row in dataset:
        row[index] = row[index]
def separarletras(dataset,letras):
    for linea in dataset:
       linea = linea.strip().split(',')
       letras.append(linea)

def contar(paises):
    contador = 1
    for i in range(len(paises)-1):
        if paises[i] == paises[i+1]:
            paises[i] = contador
            contador = contador
        elif paises[i] != paises[i+1]:
            paises[i] = contador
            contador = contador+1
    return paises
def normalFecha(valor):
    maximo = 0
    minimo = 0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,5)
def simplificarFechas(fechas):
    for dato in fechas:
        dato = dato.replace('-','')
def simplificar_Fecha(fecha):
    fecha = fecha.replace('-','')
    return fecha
def normalizacion(dataset,index):
    maxD = 10
    minD = 1
    dsT = list(zip(*dataset))
    Max = max(dsT[index])
    Min = min(dsT[index])
    print(Max)
    print(Min)
    for row in dataset:
        if row == int:
         row[index] =(maxD-minD)(row[index]-Min)/(Max-Min)+minD
def separarFilas(dataset):
    for i in range(len(dataset)):
        str(dataset[i]).split(',')
def sacarMaximo(numeros):
    maximo = 0
    for i in range(len(numeros)):
        if float(numeros[i]) > float(maximo):
            maximo = numeros[i]
    return maximo
def sacarMinimo(numeros):
    
    minimo = 1000000
    for i in range(len(numeros)):
        if float(numeros[i]) < float(minimo):
            minimo = numeros[i]
    return minimo
def normal_1(valor,minimo,maximo):
   x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
   return round(x,4)
def normal_FilaVolumenTotal_3(valor):
    maximo = 62505646.52
    minimo = 84.56
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_FilaTipo4046_4(valor):
    maximo = 22743616.17
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_filaTipo42225_5(valor):
    maximo = 20470572.61
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_filaTipo4770_6(valor):
    maximo = 2546439.11
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_bolsasTot(valor):
    maximo = 19373134.37
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_bolsasPeq(valor):
    maximo = 13384586.8
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_bolsasL(valor):
    maximo = 5719096.61
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normal_bolsasXL(valor):
    maximo = 551693.65
    minimo = 0.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def estandarizacion(dataset,index):
    dsT = list(zip(*dataset))
    prom = np.average(dsT[index])
    stdDev = np.std(dsT[index])
    for row in dataset:
        row[index] = round()
def delColumn(dataset,index):
    for row in dataset:
        del(row[index])
def convertToOrdinal(dataset, dict, index):
    for row in dataset:
        row[index] = dict[row[index]]
def filas(dataset,index):
    conjunto = []
    for row in dataset:
        conjunto.extend(row[index])
        print(conjunto)
def columnas(dataset,index,lista):
    for linea in dataset:
         try:
            fila = linea.strip().split(',')
         except ValueError:
          print('error')
         else:
               lista.append(fila[index])
    print(lista)
def converToOneHot(dataset, index):
    conjunto = set()
    for row in dataset:
        conjunto.add(row[index])

    cabecera[index:index + 1] = conjunto

    for row in dataset:
        temp = row[index]
        ceros = [0 for i in range(len(conjunto))]
        row[index:index] = ceros
        pass
def normalIndice(valor):
    maximo = 18247
    minimo = 0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)
def normalFecha(valor):
    maximo = 20180114.0
    minimo = 20150104.0
    x = (float(valor)-float(minimo)) / (float(maximo) - float(minimo))
    return round(x,4)



if __name__ == '__main__':
    data = open("avocado.csv", "r")
    cabecera = []
    dataset = []
    datasetDONE = [[0 for x in range(14)] for y in range(18248)]
    
    for linea in data:
        try:
            fila = linea.strip().split(',')
        except ValueError:
            print('error')
        else:
           dataset.append(fila)
    
    cabecera = dataset.pop(0)
    contador_Paises = 1
    for i in range(len(dataset)-1):  
     datasetDONE[i][0] = normalIndice(i)
     datasetDONE[i][1] = (normalFecha(simplificar_Fecha(dataset[i][1])))
     datasetDONE[i][2] = (dataset[i][2])
     datasetDONE[i][3] = normal_FilaVolumenTotal_3(dataset[i][3])
     datasetDONE[i][4] = normal_FilaTipo4046_4(dataset[i][4])
     datasetDONE[i][5] = normal_filaTipo42225_5(dataset[i][5])
     datasetDONE[i][6] = normal_filaTipo4770_6(dataset[i][6])
     datasetDONE[i][7] = normal_bolsasTot(dataset[i][7])
     datasetDONE[i][8] = normal_bolsasPeq(dataset[i][8])
     datasetDONE[i][9] = normal_bolsasL(dataset[i][9])
     datasetDONE[i][10] = normal_bolsasXL(dataset[i][10])
     datasetDONE[i][11] = convertTypes(dataset[i][11])
     datasetDONE[i][12] = int(dataset[i][12])
     
     if dataset[i][13] == dataset[i+1][13]:
         contador_Paises = contador_Paises
     elif dataset[i][13] != dataset[i+1][13]:
         contador_Paises = contador_Paises+1
        
     datasetDONE[i][13] = contador_Paises
    #print(normal_1(maximo=dataset[]))
    
    with open('new_dataset.csv','w',newline='') as new_file:
        writer = csv.writer(new_file,delimiter=',')
        for line in datasetDONE:
            writer.writerow(line)
            print(line)
    
    








    data.close()
