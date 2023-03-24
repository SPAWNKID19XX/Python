import random, sys

field = [0,1,2,3,4,5,6,7,8]

def checkWin(element):
    if field[0] == field[1] and field[0] == field[2] or field[3] == field[4] and field[3] == field[5] or field[6] == field[7] and field[6] == field[8] or field[0] == field[3] and field[0] == field[6] or field[1] == field[4] and field[1] == field[7] or field[2] == field[5] and field[2] == field[8] or field[0] == field[4] and field[0] == field[8] or field[2] == field[4] and field[2] == field[6]:
        print("winer " + element)
        printField()
        sys.exit()

def printField():
    print(str(field[0]) + '|' +str(field[1])+ '|' +str(field[2]))
    print('_|_|_')
    print(str(field[3]) + '|' +str(field[4])+ '|' +str(field[5]))
    print('_|_|_')
    print(str(field[6]) + '|' +str(field[7])+ '|' +str(field[8]))
    print(' | | ')

def fuelField(poss, element):
    if type(field[int(poss)]) is int:
        field[poss] = element
        checkWin(element)
    else:
        print('Error, position ' + str(poss) + ' is already fuel, Try again')
        if element == 'X':
            plTurn()
        else:
            iaTurn() 

def plTurn():
    printField()
    fuelField(int(input('Insert a position: ')), 'X')

def iaTurn():
    fuelField(random.randint(1, 9), 'O')

for i in range(9):
    if i%2 == 0:
        plTurn()
    else:
        iaTurn()
        