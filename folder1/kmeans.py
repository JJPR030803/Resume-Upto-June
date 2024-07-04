import random
import numpy
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def maximo_minimo(dsT):
    maxim = []
    minim = []
    for e in dsT:
        maxim.append(int(max(e)))
        minim.append(int(min(e)))
    return maxim, minim


def update_cent(dataset, grupos, cent):
    #cent = matriz tamaño de dataset * (centroides = 5)
    #grupos tamaño dataset
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            cent[i][j] = 0 #pone todos los valores en 0 
        cont[i] = 0
    for i in range(len(grupos)):
        for j in range(len(dataset[i])):
            cent[grupos[i]][j] += dataset[i][j] #suma el valor centroide en el indice con el valor en la misma posicion del dataset
        cont[grupos[i]] += 1
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            if cont[i] != 0:
                cent[i][j] /= cont[i]


def calcular_grupos(dataset, cent, grupos):
    continuar = False
    for ip in range(n):
        dist_min = float('+inf')
        index_min = float('+inf')
        for ic in range(k):
            dist = calcular_distancia(dataset[ip], cent[ic])#calcula la distancia de la ubicacion de un dato a un centroide
            if dist < dist_min:
                dist_min = dist
                index_min = ic#indica el indice del valor minimo
        if grupos[ip] != index_min: #si no es el minimo continua
            continuar = True
            grupos[ip] = index_min
    return continuar


def calcular_distancia(point, centroide):
    total = 0
    for i in range(m):
        total += (point[i] - centroide[i]) **2
    return total


if __name__ == '__main__':
    file = open('new_dataset.csv','r')
    k = 5 #numero centroides
    dataset = []
    for line in file:
        elem = line.strip().split(',')
        dataset.append(elem)
    cabecera = dataset.pop(0)
    n = len(dataset) # numero de renglones
    m = len(cabecera) # numero de columnas

    for i in range(n):
        for j in range(m):
            dataset[i][j] = float(dataset[i][j])
    dsT = list(zip(*dataset))
    cent = [[0 for i in range(m)] for j in range(k)] #crea centroides por cada elemento de la lista

    maximo, minimo = maximo_minimo(dsT)
    for i in range(k):
        for j in range(m):
            cent[i][j] = random.randint(minimo[j], maximo[j]) #inserta un numero aleatorio dentro del minimo/maximo de datos
    grupos = [0 for i in range(n)]#crea una lista nueva del mismo tamaño de elementos
    cont = [0 for i in range(k)]#lista del tamaño de centroides
    continuar = True

    while continuar:
        continuar = calcular_grupos(dataset, cent, grupos) #mientras no encuentre el valor minimo continua
        update_cent(dataset, grupos, cent) #actualiza los centroides 

    cont = [0 for i in range(k)]
    prom = [0 for i in range(k)]
    for i in range(n):
        prom[grupos[i]] += calcular_distancia(dataset[i], cent[grupos[i]]) #introduce el promedio de la distancia entre el valor y los centroides
        cont[grupos[i]] += 1

    for i in range(k):
        if cont[i] != 0:
            prom[i] = prom[i] / cont[i] #promedia el promedio con la lista de contadores
    prom_globalDist = numpy.average(prom) #vuelve a promediar pero ahora toda la lista

    print('Promedio Distancia Global:', prom_globalDist)

    for e in enumerate(zip(dataset, grupos)):#ennumera un conjunto del dataset y los grupos
        print(e)
    x = grupos
    
    y = [0 for _ in range(len(dataset))]
    for i in range(len(dataset)):
      y[i] = dataset[i][-2]
    
    plt.scatter(x=y,y=x,label="Probando KMEANS",color="green")
    plt.ylabel("Distancia al centroide mas cercano")
    plt.xlabel("datos")
    plt.grid(True)
    plt.show()