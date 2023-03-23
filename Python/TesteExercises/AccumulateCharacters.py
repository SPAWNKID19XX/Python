#python 3.10.8
'''
Write a function that takes a string as input and returns a new string where
each character is repeated and separated by a hyphen (-). The number of repetitions of
a character should be equal to its position in the input string, with the first
character being repeated once.
The characters in the output string should be capitalized.
'''

txt = 'cwAt'

def accum(txt):
    arr = []
    for i, latter in enumerate(txt):
        adTxt = (latter*(i+1)).capitalize()
        arr.append(adTxt)
    str = '-'.join(arr)
    return str

accum(txt)