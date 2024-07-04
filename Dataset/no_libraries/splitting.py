import csv
import random
with open("Dataset\Online Sales Data.csv","r") as file:
    listaDatos = []
    reader = csv.reader(file)
    for row in reader:
        listaDatos.append(row)
        
training_size = int(len(listaDatos) * 0.8)
test_size = len(listaDatos) - training_size

# Initialize empty lists for training and test data
training_list = []
test_list = []

# Randomly select data for training set
for _ in range(training_size):
    index = random.randrange(len(listaDatos))
    training_list.append(listaDatos.pop(index))
    
test_list = listaDatos


print(len(training_list))
print(len(test_list))

    
    
