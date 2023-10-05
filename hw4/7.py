import numpy as np
lst = [10,20,30,40,50]
vctr = np.array(lst)
print(vctr)


import random
m = input("m = ")
n = input("n = ")
Matrix = []
for i in range(m):
    row = []
    for j in range(n):
        randNumber = random.randint(1, 11)
        row.append(randNumber)
    Matrix.append(row)
print('Matrix M:')
for i in range(m):
    print(Matrix[i])