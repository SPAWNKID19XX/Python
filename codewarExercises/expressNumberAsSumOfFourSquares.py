from math import sqrt
import random
n= random.randint(2**10, 2**15)

a = int(sqrt(n))
b = int(sqrt(n-a**2))
c = int(sqrt(n-a**2-b**2))
d = int(sqrt(n-a**2-b**2-c**2))
print(a, b, c, d, n)
