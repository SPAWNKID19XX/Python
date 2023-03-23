#python 3.10.8

'''
Write a function that determines if there exists a positive integer k such that the sum of the digits of a
given positive integer n, taken to successive powers of p, is equal to k times n.
In other words, the function should return k if the following equation holds:
(a^p + b^(p+1) + c^(p+2) + d^(p+3) + ...) = n * k
where a, b, c, d are the digits of n.
If no such positive integer k exists, the function should return -1.
'''

a = 695
b = 2

def dig_pow(num, p):
    total = 0
    for obj in str(num):
        total += int(obj)**p
        p += 1
    total /= num
    if int(total)==total:
        return (int(total))
    else:
        return -1

print(dig_pow(a,b))