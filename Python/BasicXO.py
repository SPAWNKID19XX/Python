import random, sys
player = 100
field = []

for i in range(9):
    field.append(i)

def checkWin(element):
    if field[0] == field[1] and field[0] == field[2] or field[3] == field[4] and field[3] == field[5] or field[6] == field[7] and field[6] == field[8] or field[0] == field[3] and field[0] == field[6] or field[1] == field[4] and field[1] == field[7] or field[2] == field[5] and field[2] == field[8] or field[0] == field[4] and field[0] == field[8] or field[2] == field[4] and field[2] == field[6]:
        print("winer " + element)
        sys.exit()


def printField():
    print(str(field[0]) + '|' +str(field[1])+ '|' +str(field[2]))
    print('_|_|_')
    print(str(field[3]) + '|' +str(field[4])+ '|' +str(field[5]))
    print('_|_|_')
    print(str(field[6]) + '|' +str(field[7])+ '|' +str(field[8]))
    print(' | | ')

def fuelField(poss, element):
    if checkCell(poss) == True:
        field[poss] = element
        checkWin(element)
    else:
        print('Error, position is already fuel')

def checkCell(position):
    if type(field[int(position)]) is int:      
        return True
    else:
        return False

def plTurn():
    xo = 'X'
    printField()
    pl= int(input('Insert a position: '))
    fuelField(pl, xo)
    return pl

def iaTurn():
    xo = 'O'
    ia  = random.randint(0, 8)
    fuelField(ia, xo)
    return int(ia)

for i in range(9):
    if i%2 == 0:
        plTurn()
    else:
        iaTurn()