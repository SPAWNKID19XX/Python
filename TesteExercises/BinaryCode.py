#python 3.10.8
'''
Write a function that takes in an array of ones and zeroes,
and converts the equivalent binary value to an integer.
'''
a = [1,0,1,1,0,0,1,0]

def binToInt(arr):
    num=''.join(str(ell) for ell in arr)
    return int(num,2)


print(binToInt(a))
