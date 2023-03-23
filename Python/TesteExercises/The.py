#python 3.10.8
'''
The goal of this exercise is to convert a string to a new string where each character in the new string is represented
by "(" if it appears only once in the original string, or ")" if it appears more than once.
The case of the characters should be ignored.
'''

txt = '(( @'

def newStr(txt):
    res = ''
    for latter in txt.lower():
        if txt.count(latter) > 1:
            res += ')'
        else:
            res += '('
    return res

lol = newStr(txt)
print(lol)