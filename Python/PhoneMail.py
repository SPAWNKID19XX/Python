#python3
#will find all phone numbers and email andess from text

import re, pyperclip

#Phone regex
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #regione code
    (\s|-|\.)?          #separator
    (\d{3})             #first 3 numbers
    (\s|-|\.)?          #separator
    (\d{4})             #last 4 numbers
    (\s*(ext|x|ext.)\s* (\d{2, 5}))?
)''', re.VERBOSE)

#Email regex
mailRegex = re.compile(r''''(
    [a-zA-Z0-9._%+-]+   #UserName
    @ #separador
    [a-zA-Z.-]+ #Domen
    (\.[a-zA-Z] {2, 4}) #lang
)''',re.VERBOSE)

#find a simulat text from spting from clipboard
#first we will copy a text in clipboard and get Phone Numbers from a text

text = str(pyperclip.paste())
list = []
for groups in phoneRegex.findall(text):
    phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNumber += ' x' + groups[8]
    list.append(groups[0])

for groups in mailRegex.findall(text):
    list.append(groups[0])

#copy result to clipboard
if len(list) > 0:
    pyperclip.copy('\n'.join(list))
    print('Copied to clipboard')
    print('\n'.join(list))
else:
    print('No Telephone or email adress')