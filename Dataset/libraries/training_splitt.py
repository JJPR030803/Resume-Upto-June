import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("Dataset\Online Sales Data.csv")

df = dataset.dropna(subset=["Total Revenue"])

x = df.drop(columns=["Total Revenue", 'Transaction ID', 'Date', 'Product Name'])

y = df["Total Revenue"]


x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)


print("X_train:\n", x_train)
print("X_test:\n", x_test)


