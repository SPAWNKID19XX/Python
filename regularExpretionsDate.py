#python3
#script will find all date by regular expresions
#costomize it by the same format and print it
#Ideal format is DD-MM-YYYY

import re
from turtle import ycor

msg = '''My birthday is 6/8/1987, 
Aaron\'s birthday is 18-03-2013, 
Mum\'s birthsday is 07.05.1985, 
Emily\'s birthday is 07.02.2018,
Vlad\'s birthday is 40.02.2018,
Serjon\'s birthday is 07.02.2018,
Alexey\'s birthday is 23-08.1983
Charley\'s birthday is 07.02.2018,
Arsen\'s birthday is 07.02.2018,
Oscar\'s birthday is 07.02.2018,
'''

#declare a regular expresions
yearRegex = re.compile(r'''(
    (\d\d?)             #day
    (\s|-|/|\.)          #separator
    (\d\d?)             #month
    (\s|-|/|\.)          #separator
    (\d{4})             #year
)''', re.VERBOSE)
#declare variables
month31Day = ['01', '05', '07', '08', '10', '12']
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

def checkDate(date):
    splitDate = date.split('/')
    daySplit = splitDate[0]
    monthSplit = splitDate[1]
    yearSplit = splitDate[2] 
    #print(daySplit, monthSplit, yearSplit)
    #print(splitDate) 
    
    if int(yearSplit) % 4 == 0:
        if int(monthSplit) == '02':
            if int(daySplit) > 29:
                return  False
    
    if monthSplit not in month31Day:
        if int(daySplit) > 30:
            return False
        else:
            return True
    else:
        if int(daySplit) > 31:
            return False
        else:
            return True 
    
#print my list and function CHECKDATE checking if date exist
for list in range(len(listData)):
    printDate = '/'.join(listData[list])
    resTF = checkDate(printDate)
    print(printDate + ' = ' + str(resTF) )