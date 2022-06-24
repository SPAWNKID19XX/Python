from ast import Not


name = ''

while not name:
    print('Insert your name')
    name = input()

print('Hello ' + str(name) + ' how many guests did you invited')
numOfGuests = int(input())

if numOfGuests:
    print('Do not forget reserve a seats')

print('Finish')