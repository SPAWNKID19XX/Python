#Python 3.10.8
'''
Write a function that takes in an array of integers and returns an index N
such that the sum of the integers to the left of N
is equal to the sum of the integers to the right of N.
If no such index exists, the function should return -1.
The function should return the lowest index in case of multiple valid answers.
'''

a = [20, 1000, -80, 10, 10, 15, 35]

def retIndex(arr):
    for i, obj in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

res = retIndex(a)
print(res)