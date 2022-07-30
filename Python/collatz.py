from ast import Try


def collatz(number):
    if number%2 == 0:
        res = number / 2
    else:
        res = 3 * number + 1
    return res

num = 0
while num < 2 or num > 10:
    try:
        num = int(input('Insert a number between 2 to 10: '))
    except:
        print('Error, Invalid argument, must be Integer Number')

while num != 1:
    num = int(collatz(num))
    print(num)