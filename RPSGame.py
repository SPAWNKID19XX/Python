import random, sys
drow = 0
wins = 0
lose = 0

def checkWin(player, ia):
    global drow
    global wins
    global lose
    if (player == 1 and ia == 1) or (player == 2 and ia == 2) or (player == 3 and ia == 3):
        print('Drow')
        drow += 1
        print('D:' + str(drow) + 'W:' + str(wins) + 'L:' + str(lose))
        return 1
    elif (player == 1 and ia == 2) or (player == 2 and ia == 3) or (player == 3 and ia == 1):
        print('Win')
        wins += 1
        print('D:' + str(drow) + 'W:' + str(wins) + 'L:' + str(lose))
        return 2
    elif (player == 1 and ia == 3) or (player == 3 and ia == 2) or (player == 2 and ia == 1):
        print('Lose')
        lose += 1
        print('D:' + str(drow) + 'W:' + str(wins) + 'L:' + str(lose))
        return 3
    else:
        lose += 1
        print('D:' + str(drow) + 'W:' + str(wins) + 'L:' + str(lose))
        return 4 

def printPossibleElements():
    print('1 = Rock, 2 = Scissor, 3 = paper , 100=exit')

def printChouse(element):
    #print(type(element))
    if element == 1:
        print('Rock')
    elif element == 2:
        print('Scissor')
    elif element == 3:
        print('Paper')
    else:
        print('Rogue, Element do not exist')        

def playerTurn():
    printPossibleElements()
    print('Your turn')
    pl = int(input())
    if pl == 100:
        sys.exit()
    printChouse(pl)
    return pl

def iaTurn():
    ia = random.randint(1, 3)
    printChouse(ia)
    return ia

while True:
    checkWin(playerTurn(), iaTurn())