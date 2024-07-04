from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


dataset = pd.read_csv("Dataset\Online Sales Data.csv")
ct_product_category = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[2])],remainder="passthrough",)
columnas_categoricas = dataset.iloc[:,]
product_one = ct_product_category.fit_transform(columnas_categoricas)

product_one = pd.DataFrame


df = product_one.dropna(subset=["Total Revenue"])

x = df.drop(columns=["Total Revenue", 'Transaction ID', 'Date', 'Product Name'])

y = df["Total Revenue"]


x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)




