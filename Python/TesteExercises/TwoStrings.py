#Python 3.10.8
'''
"Write a function that takes in two strings, s1 and s2, containing only letters from 'a' to 'z'.
The function should return a new string, containing distinct letters in alphabetical order, each taken only once
from either s1 or s2. The returned string should be the longest possible.

Examples:
●	The function called with the inputs 'xyaabbbccccdefww' and 'xxxxyyyyabklmopq' should return 'abcdefklmopqwxy'.
●	The function called with the inputs 'abcdefghijklmnopqrstuvwxyz' and 'abcdefghijklmnopqrstuvwxyz' should return
'abcdefghijklmnopqrstuvwxyz'."
'''

s1 = 'xyaabbbccccdefww'
s2 = 'xxxxyyyyabklmopq'
def retAlf(s1, s2):
    setA = set(s1)
    setB = set(s2)
    setC = setB.union(setA)
    setC = sorted(setC)
    res = ''.join(setC)
    return res




print(retAlf(s1, s2))