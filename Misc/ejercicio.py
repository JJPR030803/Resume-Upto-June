import random as rd
from numpy.random import rand,randint

N = 1000000
counterMenos = 0
counterMas = 0

for i in randint(low=0,high=N,size=N):
    if(i < N/2):
        counterMenos+=1
    elif(i>N/2):
        counterMas+=1

percentages = {"Cabeza:":counterMas/N,"Cola:":counterMenos/N}


print(percentages)
