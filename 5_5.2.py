from collections import deque
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')

fruits.count('tangerine')
fruits.index('banana')
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft()
squares = []

for x in range(10):

    squares.append(x**2)
    
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
combs = []

for x in [1,2,3]:

    for y in [3,1,4]:

        if x != y:

            combs.append((x, y))
matrix = [

    [1, 2, 3, 4],

    [5, 6, 7, 8],

    [9, 10, 11, 12],

]
[[row[i] for row in matrix] for i in range(4)]
transposed = []

for i in range(4):

    transposed.append([row[i] for row in matrix])
    
transposed = []

for i in range(4):

    # the following 3 lines implement the nested listcomp

    transposed_row = []

    for row in matrix:

        transposed_row.append(row[i])

    transposed.append(transposed_row)
    
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]

