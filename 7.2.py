import json
import pickle
with open('example.txt', 'w') as f:
    f.write('This is a sample text.\n')

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
    


# Writing JSON to a file
data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading JSON from a file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
    


# Writing a Python object to a file
grades = {'Alice': [90, 95, 88], 'Bob': [85, 92, 78]}
with open('grades.pkl', 'wb') as f:
    pickle.dump(grades, f)

# Reading a Python object from a file
with open('grades.pkl', 'rb') as f:
    loaded_grades = pickle.load(f)
    print(loaded_grades)