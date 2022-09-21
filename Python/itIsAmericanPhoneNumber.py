#python3
#script will check if a string introdused by user is
#American Phone Number

msg = 'My number is 096-469-6149, my wife\'s number is 096-469-6179.Call me as soon, as it is possibol'
#inputText = input('Insert American phone Number: ')

def checkingIfAmericanPhoneNumber(text):
    #checking number of simbols in text
    if len(text) != 12:
        return False
    else:
        for elements in range(0, 3):
            if not text[elements].isdecimal():
                return False
        if text[3] != '-' :
            return False
        for elements in range(4, 7):
            if not text[elements].isdecimal():
                return False
        if text[7] != '-' :
            return False
        for elements in range(8, 12):
            if not text[elements].isdecimal():
                return False
        return True

def findNumbers(text):
    numberList = []
    #try to find and append to list all numbers
    for i in range(len(text)):
        text12Simbols = text[i : i+12]
        if (checkingIfAmericanPhoneNumber(text12Simbols)):
            numberList.append(text12Simbols)
    #print a list in table
    for i in range(len(numberList)):
        print(str(i+1) + ' Number is ' + numberList[i])

findNumbers(msg)