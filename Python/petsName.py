from operator import index


namesPets = ['Sophy', 'Kinder', 'Aaron', 'Emy', 'Eevee']

nameMyPet = str(input('Find your Pet Name: '))

try:
    print('your pet is here. INDEX=' + str(namesPets.index(nameMyPet)))
except:
    print('your pet is not here')
