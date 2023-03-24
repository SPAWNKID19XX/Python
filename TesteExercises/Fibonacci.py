#python 3.10.8
'''
Write a function that generates the first n elements of the Tribonacci sequence,
given a starting signature of 3 integers. The Tribonacci sequence is similar to the
Fibonacci sequence, but the next element is obtained by summing the last 3
elements of the sequence instead of the last 2.
'''

arr = [1,1,1]
n = 0

def tribanachi(arr, n):
    if n == 0:
        arr.clear()
    while len(arr) < n:
        arr.append(sum(arr[-3:]))
    return arr

print(tribanachi(arr, n))