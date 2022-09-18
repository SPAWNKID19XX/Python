#python3
#script will check if a string introdused by user is
#American Phone Number

msg = 'My number is 096-469-6149, my wife\'s number is 096-469-6179.Call me as soon, as it is possibol'
#inputText = input('Insert American phone Number: ')


def searchNumber(text):
    for i in range(len(text)):
        phoneNumber = text[i:i +12]
        if checkingIfAmericanPhoneNumber(phoneNumber):
            print('yesss')


def checkingIfAmericanPhoneNumber(text):
    #checking number of simbols in text
    print(len(text))
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

def answerTF(answer):#return true if is or False if not American number
    print(answer)
    if (answer == True):
        print('Yes, is American number')
    else:
        print('No, isn\'t American number')
