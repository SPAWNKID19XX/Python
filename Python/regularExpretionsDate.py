#python3
#script will find all date by regular expresions
#costomize it by the same format and print it
#Ideal format is DD-MM-YYYY


from cgi import print_arguments
import re
from traceback import print_list

msg = '''My birthday is 6/8/1987, Aaron\'s birthday is 18-03-2013, Mum\'s birthsday is 07.05.1985, Emily\'s birthday is 7.02.2018'''

#declare a regular expresions
yearRegex = re.compile(r'''(
    (\d\d?)             #day
    (\s|-|/|\.)          #separator
    (\d\d?)             #month
    (\s|-|/|\.)          #separator
    (\d{4})             #year
)''', re.VERBOSE)

listData = []
#costomize and append correct format data in my list
for groups in yearRegex.findall(msg):
    date = '/'.join([groups[1], groups[3], groups[5]])
    grpsAfterSplit = date.split('/')
    for i in range(len(grpsAfterSplit)):
        if len(grpsAfterSplit[i]) < 2:
            oldObj = grpsAfterSplit[i]
            grpsAfterSplit[i] = '0' + oldObj
    listData.append(grpsAfterSplit) 

#print my list
for list in range(len(listData)):
    print('/'.join(listData[list]))