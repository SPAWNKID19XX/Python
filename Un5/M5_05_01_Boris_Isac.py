import numpy
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

cubo1 = np.random.random([3,3,3])
cubo2 = np.random.random([3,3,3])

vetor = np.arange(3,12)
b = np.reshape(vetor, [3,3])
print(b)

print (cubo1==cubo2)#1 comparison of each of elements from both matrix
comparison = numpy.array_equal(cubo1,cubo2)#2 comparison of matrix
print(comparison)

