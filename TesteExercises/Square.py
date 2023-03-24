#Python 3.10.8
'''
Write a function that determines whether a given integer is a perfect square.
A perfect square is an integer that is the product of some integer with itself.
'''
import math
def isSqr(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False

print(isSqr(0))
