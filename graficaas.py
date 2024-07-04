import random
import csv
import matplotlib.pyplot as plt
def fechasToInt(listafechas):
    listaLista = []
    for i in range(len(listafechas)):
        fecha = listafechas[i]
        listaLista.append(listafechas[i].replace('-',''))
    return listaLista
                
def educacion(data):
    for i in range(len(data)):
        if data[i] == 'Basic':
            data[i] = 1
        elif data[i] == '2n Cycle':
            data[i] = 2
        elif data[i] == 'Graduation':
            data[i] = 3
        elif data[i] == 'Master':
            data[i] = 4
        elif data[i] == 'PhD':
            data[i] = 5
    return data
def casado(data):
    for i in range(len(data)):
        if data[i] == 'Single':
             data[i] = 1
        elif data[i] == 'Divorced':
            data[i]=2
        elif data[i] == 'Together':
            data[i] = 3
        elif data[i] == 'Married':
            data[i] = 4
        elif data[i] == 'Widow':
            data[i] = 5
        else:
            data[i] = 10
    return data
    
def maximMinim(dst):
    maxim = []
    minim = []
    for i in dst:
        maxim.append(max(i))
        minim.append(min(i))
    return maxim,minim
def Graph(dsT,grupos,centroides = None):
    colors = dict()
    grupColor = [e * 50 for e in grupos]
    fig, ax = plt.subplots()
    ax.scatter(dsT[0],dsT[10],c = grupColor)
    CT = list(zip(*centroides))
    ax.scatter(CT[0],CT[1],color="red")
    plt.show()
    plt.close()
def crearCSV(filecsv,datasetL):
    filasRow = []
    contador = 0
    with open(filecsv,'w',newline='') as csvarchivo:
        writers = csv.writer(csvfile=csvarchivo,)
        for i in range(len(dataset[0])):
         filasRow.append(contador+1)
         writers.writerow()
    csv.writer(csvfile=filecsv)
if __name__ == '__main__':
    file = open("marketing_campaign.csv","r")
    cabecera = []
    datosRandom = []
    filaEducacion = []
    filaCasado = []
    dataset = []
    originalG = []
    filaIncome = []
    filaTeen = []
    filaKid = []
    filaDTcostumer = []
    for line in file:
        try:
          elem = line.strip().split("\t")
        except ValueError:
            print('Error')
        else:   
         dataset.append(elem)
         filaEducacion.append(elem[2])
         filaCasado.append(elem[3])
         filaIncome.append(elem[4])
         filaKid.append(elem[5])
         filaTeen.append(elem[6])
         filaDTcostumer.append(elem[7])
         
    cabecera = dataset.pop(0)
    dsT = list(zip(*dataset))
    maxim,minim = maximMinim(datosRandom)
    crearCSV(filecsv="marketing_campaignclean.csv",datasetL=cabecera)
    print(cabecera)
    #for i in range(len(dataset)):
     #print(dataset[i][2])
    #print(max(maxim),min(minim))