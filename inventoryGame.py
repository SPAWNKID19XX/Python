import pprint

stuff = {'Arrow' : 12, 'Rope': 1, 'Torch': 6, 'GoldCoin': 42,'Knife': 1}
dragonLoot = ['GoldCoin', 'Knife', 'GoldCoin', 'GoldCoin', 'Ruby']

def displayInventory(list):
    totalObjects = 0
    print('Inventory:')
    for key, value in list.items():
        print(str(value) + ' ' + key)
        totalObjects += list[key]
    print('Total Items = ' + str(totalObjects))

def addToInventory(stuff, addItem):
    for i in range(len(addItem)):
        stuff.setdefault(addItem[i], 0)
        stuff[addItem[i]] += 1
    print(stuff)

print('Before Looting')
displayInventory(stuff)
addToInventory(stuff, dragonLoot)
print('After Looting')
displayInventory(stuff)
