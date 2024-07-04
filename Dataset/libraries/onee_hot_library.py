from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


dataset = pd.read_csv("Dataset\Online Sales Data.csv")
ct_product_category = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[2])],remainder="passthrough",)
columnas_categoricas = dataset.iloc[:,]
product_one = ct_product_category.fit_transform(columnas_categoricas)



print(product_one[0])


#x = ct.fit_transform()