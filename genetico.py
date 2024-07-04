import random as rd
import numpy as np
import math
import os

if __name__ == "__main__":
    archivos = os.listdir("TSP Instances")
    for archivo in archivos:
        n = 10
        pop_size = 200
        p = [[i for i in range(n)] for j in range(int(pop_size/2))]
        vo = [0 for i in range(pop_size)]
        vivos = [False for i in range(pop_size)]
        file = open("TSP Instances/{0}".format(archivo),"r")
        file.readline()
        file.readline()
        file.readline()
        n = int(file.readline().strip().split(":")[1])
        file.readline()
        file.readline()
        cities = np.zeros((n,2))
        for i in range(n):
            cities[i] = file.readline().strip().split(" ")[1:]
        n = 10
        graph = np.zeros((n,n))
        for i in range(n-1):
            for j in range(i+1,n):
                graph[i][j] = int(math.sqrt((cities[i][0]-cities[j][0])**2))
                graph[j][i] = graph[i][j]
        n=10
        for i in range(len(p)):
            vivos[i] = True
            for j in range(n-1):
                it = rd.randint(j,n-1)
                temp = p[i][it]
                p[i][it] = p [i][j]
                p[i][j] = temp
        p.extend([[0 for i in range(n)] for j in range(int(pop_size/2))])
        itersSinMejora = 10
        BestGlobal = float("+Inf")
        limiteMuerte = int(pop_size*.75)
        while itersSinMejora > 0:
            itersSinMejora -= 1
            for i in range(pop_size):
                if vivos[i] == False:
                    p1 = rd.randint(0,pop_size-1)
                    while (vivos[p1 == False]):
                        p1 = rd.randint(0,pop_size-1)
                    p2 = rd.randint(0,pop_size-1)
                    while(vivos[p2] == False or p2 == p1):
                        p2 = rd.randint(0,pop_size-1)
                    j1 = rd.randint(0,n)
                    j2 = rd.randint(0,n)
                    if j2 < j1:
                        temp = j2
                        j2 = j1
                        j1 = temp
                    seleccionados = [0 for i in range(n)]
                    for j in range(n):
                        p[i][j] = -1
                    for j in range(j1,j2):
                        p[i][j] = p[p1][j]
                        seleccionados[p[p1][j]] = 1
                    j2 = 0
                    for j1 in range(n):
                        while j2<n and p[i][j2] != -1:
                            j2 += 1
                        if seleccionados[p[p2][j1]] == 0:
                            p[i][j2] = p[p2][j1]
                            j2 += 1
                for i in range(pop_size):
                   vivos[i] = True
                
                for i in range(pop_size):
                    vo[i] = 0
                    for j in range(n-1):
                        vo[i] += graph[p[i][j]][p[i][j+1]]
                    vo[i] += graph[p[i][-1]][p[i][0]]
                minactual = min(vo)
                if minactual < BestGlobal:
                    BestGlobal = minactual
                    itersSinMejora = 10
                prom = np.average(vo)
                muertos = 0
                for i in range(pop_size):
                    if vo[i] > prom:
                        vivos[i] = False
                        muertos += 1
                        if muertos >= limiteMuerte:
                            break
        BestGlobal = min(vo)
        print("Archivo = {0} BestGlobal = {1}".format(archivo,BestGlobal))