#python 3.10.8
'''
In this task, you are required to replace every letter in a given string with
its position in the alphabet. If the string contains any non-letter
characters, ignore them and do not include them in the output.
For example, the letter "a" should be replaced with "1", "b"
should be replaced with "2", and so on.
'''

txt = 'Hello World!!!'
def alfabet_position(txt):
    #ascii 'a' = 97-1(index[0])
    res = ' '.join(str(ord(latter)-96) for latter in txt.lower() if latter.isalpha())
    return res

res = alfabet_position(txt)
print(res)