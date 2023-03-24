#python3
#script check if a inputStrin is realy hight level Password

import re
passRegex = re.compile(r'''
    [a-z]+
    [A-Z]+
    [0-9]+
''', re.VERBOSE)

password = input('Insert a PassWord: ')
pw = passRegex.search(password)
if pw:
    print('Password Accepted')
else:
    print('PassWord should contain at least 8 simbols, \nat list 1 UPPERCASE and LOWERCASE simbol \nand at least 1 number')
