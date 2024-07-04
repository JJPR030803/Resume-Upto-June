import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer #Impute sirve para valores vacios usando media,promedio,etc
dataset = pd.read_csv("Dataset\Online Sales Data.csv")
x = dataset.iloc[:,:-2]
y = dataset.iloc[:,0].values

listaTest = dataset.iloc[:,4:7]

imputer = SimpleImputer(missing_values=np.nan,strategy="most_frequent")

imputer.fit(listaTest)
listaImpute = imputer.transform(listaTest.copy())

print(listaTest)
print(listaImpute)


#print(dataset)