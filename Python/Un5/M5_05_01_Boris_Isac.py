import numpy as np

print(np.__version__)

arr = np.arange(10,100,10)
print('Array: \n',arr)
print('Invert Array: \n',arr.__invert__()+1)

vetor = np.arange(0,9)
matrix = np.reshape(vetor, [3,3])
print('Matrix:\n',matrix)

matrixIdentity = np.identity(6)
print('Identidade:\n',matrixIdentity)

cubo = np.random.random([3,3,3])
print(cubo)

vetor = np.arange(3,12)
b = np.reshape(vetor, [3,3])
print(b)

print (b==matrix)