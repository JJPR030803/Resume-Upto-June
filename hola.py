print("Hola mundo")
print (50-5*6)
print("doesn't")
print('"Yes, they said')
print(17/3)
print(5 ** 2)
print(25 ** .5)
print('C:some\\name')
print(r'C:some\name')
word = "Hola mundo"
print(word[-9])
print(word[:4])
print(word[2:])
print(word[2:6])

for i in range(5,10):
    print (i)

def fibonacci(a,b):
    while a < 10:
        print(a)
        a,b = b, a+b
        

fibonacci(0,1)