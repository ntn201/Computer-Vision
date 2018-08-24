import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
b = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

c = np.dot(a,b)

res = 1/9*sum(c)/3

print(c)