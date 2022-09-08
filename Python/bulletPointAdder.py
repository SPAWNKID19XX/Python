<<<<<<< HEAD
#python 3
#put * before animal names and copy all lines to clipboard
from functools import update_wrapper
import pyperclip

#Original String Line
print('ORIINAL TEXT')
text = 'Animals List \nFishes List \nBiologist List \nPlants List'
print(text)
pyperclip.copy(text) #!copy a text in clipboard

#record Original String in array ARR
#separator '\n' post with argument to method split
arr = text.split('\n')
for i in range(len(arr)):
    arr[i] = '* ' + arr[i]

#to Make: Devide a lines, post a stars(*) before each line
#changed text with stars before lists
print('changed text with stars before lists.'.upper())
text = '\n'.join(arr)
pyperclip.copy(text)
=======
#python 3
#put * before animal names and copy all lines to clipboard
from functools import update_wrapper
import pyperclip

#Original String Line
print('ORIINAL TEXT')
text = 'Animals List \nFishes List \nBiologist List \nPlants List'
print(text)
pyperclip.copy(text) #!copy a text in clipboard

#record Original String in array ARR
#separator '\n' post with argument to method split
arr = text.split('\n')
for i in range(len(arr)):
    arr[i] = '* ' + arr[i]

#to Make: Devide a lines, post a stars(*) before each line
#changed text with stars before lists
print('changed text with stars before lists.'.upper())
text = '\n'.join(arr)
pyperclip.copy(text)
>>>>>>> 2e949e990693a6f7fd6e5331c39ade638c4d7d45
print(text)