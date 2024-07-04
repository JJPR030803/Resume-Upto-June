from sklearn.preprocessing import LabelEncoder

binario = LabelEncoder()

lista = ['si','no','si','no',"hola","perro"]
lista = sorted(lista)
print(lista)
lista = binario.fit_transform(lista)

print(lista)