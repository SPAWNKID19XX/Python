#python 3.10.8
'''
Write a function that takes a string as input and returns a boolean indicating whether
or not the string is a pangram. A pangram is a sentence that contains every single letter
of the alphabet at least once.
The function should ignore numbers, punctuation, and the case of the letters.
'''

txt = 'The quick brown fox jumps over the lazy cat'

def isPangram(txt):
    myDict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
              'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    if len(txt) < 26:
        return False
    for ch in txt.lower():
        if ch.isalpha():
            myDict[ch] += 1
    if 0 in myDict.values():
        return False
    else:
        return True


print(isPangram(txt))