import random

count = 0
secretNumber = random.randint(0, 20)
guessNumber = -1
while guessNumber != secretNumber :
    count += 1
    guessNumber = int(input('Guess a number: '))
    if secretNumber < guessNumber:
        print('secretNumber < ' + str(guessNumber))
    elif secretNumber > guessNumber:
        print('secretNumber > '  + str(guessNumber))
    else:
        print('secretNumber = ' + str(secretNumber))
        print('you guessed by ' + str(count))
        break