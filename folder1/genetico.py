import math
import random as rand
import numpy as np
import os

if __name__ == "__main__":
    archivos = os.listdir("TSP Instances")
    for archivo in archivos:
        #region inicializa variables
        n = 10
        pop_size = 200
        p = [[i for i in range(n)] for j in range(int(pop_size/2))]
        vo = [0 for i in range(pop_size)]
        vivos = [False for i in range(pop_size)]
        #endregion
        #region Lenxtura
        file = open("TSP Instances/{0}".format(archivo),"r")
        file.readline()
        file.readline()
        file.readline()
        try:
          n = int(file.readline().strip().split(":")[1])#numero de valores en archivo seleccionado
        except ValueError:
           n = n
        file.readline()
        file.readline()
        #cities = np.zeros((n,2))#llena una lista de 0 dentro de una lista valores=[0.0.]
        cities = [[0 for _ in range(2)] for _ in range(n)]
        
        for i in range(n):
             cities[i] = (file.readline().strip().split(" ")[1:])
           
        graph = [[0 for _ in range(n)] for _ in range(n)]
        #np.zeros(((n,n)))
        for i in range(n-1):
            for j in range(i+1,n-1):
                graph[i][j] = int(math.sqrt((float(cities[i][0])-float(cities[j][0]))**2))
                graph[j][i] = graph[i][j]
                
        n = 10
        #endregion
        #region Inicializa P
        for i in range(len(p)):
            vivos[i] = True
            for j in range(n-1):
                it = rand.randint(j,n-1)
                temp = p[i][it]
                p[i][it] = p[i][j]
                p[i][j] = temp

        p.extend([[0 for i in range(n)] for j in range(int(pop_size/2))])
        #endregion
        itersSinMejora = 20
        BestGlobal = float("+Inf")
        limiteMuerte = int(pop_size * .9)
        while itersSinMejora > 0:
            itersSinMejora -= 1
            #region Cruza y Muta (no muta po lo pronto
            for i in range(pop_size):
                if vivos[i] == False:
                    p1 = rand.randint(0,pop_size-1)
                    while (vivos[p1] == False):
                        p1 = rand.randint(0, pop_size -1)

                    p2 = rand.randint(0,pop_size-1)
                    while (vivos[p2] == False or p2 == p1):
                        p2 = rand.randint(0, pop_size - 1)
                    j1 = rand.randint(0,n)
                    j2 = rand.randint(0,n)
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
                        while j2 < n and p[i][j2] != -1:
                            j2 += 1
                        if seleccionados[p[p2][j1]] == 0:
                            p[i][j2] = p[p2][j1]
                            j2 += 1
            for i in range(pop_size):
                vivos[i] = True
            #endregion
            #region Evaluacion y Seleccion Elitista
            for i in range(pop_size):
                vo[i] = 0
                for j in range(n-1):
                    vo[i] += graph[p[i][j]][p[i][j+1]]
                vo[i] += graph[p[i][-1]][p[i][0]]
            minActual = min(vo)
            if minActual < BestGlobal:
                BestGlobal = minActual
                itersSinMejora = 20
            prom = np.average(vo)
            muertos = 0
            for i in range(pop_size):
                if vo[i] > prom:
                    vivos[i] = False
                    muertos += 1
                    if muertos >= limiteMuerte:
                        break
            #endregion

        BestGlobal = min(vo)
        print("Archivo = {0} BestGlobal = {1}".format(archivo,BestGlobal))

        """for e in enumerate(zip(p,vo,vivos)):
         print(e)"""