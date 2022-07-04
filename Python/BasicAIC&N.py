from dataclasses import field
import random

field = []
playerPosChouse = "0"
for i in range(0, 9):
    field.append(i)

def checkWin():
    if field[0] == field[1] and field[0] == field[2] or field[3] == field[4] and field[3] == field[5] or field[6] == field[7] and field[6] == field[8] or field[0] == field[3] and field[0] == field[6] or field[1] == field[4] and field[1] == field[7] or field[2] == field[5] and field[2] == field[8] or field[0] == field[4] and field[0] == field[8] or field[2] == field[4] and field[2] == field[6]:
        print("winer")


def printField():
    print(str(field[0]) + '|' +str(field[1])+ '|' +str(field[2]))
    print('_|_|_')
    print(str(field[3]) + '|' +str(field[4])+ '|' +str(field[5]))
    print('_|_|_')
    print(str(field[6]) + '|' +str(field[7])+ '|' +str(field[8]))

printField()

while True:
    while True: 
        print('Player, your turn')
        playerPosChouse =  input()
        if isinstance(field[int(playerPosChouse)], int)  == True :
            field[int(playerPosChouse)] = "X"
            printField()
            break
        print('A Cell is not empty')
        if checkWin() == True:
            print('Player Is Winer')
            break
    while True:
        print("AI's turn")
        aiChouse = random.randint(1, 9)
        if isinstance(field[int(aiChouse)], int) == True :
            field[int(aiChouse)] = "O"
            printField()
            break
        print('A Cell is not empty')
        if checkWin() == True:
            print('AI Is Winer')
            break
"""
print('Basic AI for Cross&Nought')
print('GameField represent 3X3 cels. A turns alternate between player and AI')
print('A player should to collect 3Xs in row or column or diagonal before a AI to win')
print('A numbers on field coressponde a position. A player will change a position from 1 until 9')
"""