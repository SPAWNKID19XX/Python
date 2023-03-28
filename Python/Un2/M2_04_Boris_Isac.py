print("Exercise 1 (List and tuple)".center(100).upper())
members = ("Mike Shinoda", "Brad Delson", "Rob Bourdon", "Joe Hahn", "Dave Farrell")
role = ["Keyboardist", "DJ", "Vocal", "Guitarist", "Drummer"]
print("Create and print List and Tuple")
print(members)
print(role)

print("\nPrint secound elemente from List and penultimate of Tuple ")
print(role[1], " --> ", members[-2])

print("\nChange and reprint list. tuple is immutable")
role[0] = "Vocal"
role[2] = "Keyboardist"
print(members)
print(role)


print("\nSize List: ", len(role))
print("Size Tuple: ", len(members))

print("\nChester Charles Bennington in Tuple MEMBERS: ", ("Chester Charles Bennington" in members))
print("Vocal in List ROLE: ", ("Vocal" in role))

print("\nAdd some elements in List and Tuple and reprint")
role.append("Bassist")
members = members + ("Chester Charles Bennington",)
print("Eu sei que sou batoteiro, mas......\n\t", members)
print("\t", role)

print("\nDelete all elements in List and Tuple")
role.clear()
members = []
print(members)
print(role)

print("Exercise 2 (Sets and Dict)".center(100).upper())
print("Create and print SETS and DICT")
cars = {"Nissan", "BMW", "Renault", "MiniCooper", "VW"}
founded = {"Nissan": 1933, "BMW": 1917, "Renault": 1899, "MiniCooper": 1959, "VW": 1937}

for key in cars:
    print("SET(DICT Key) --->", key.rjust(12, " "), "\tExist in DICT value {:7}".format(founded[key]))

print("\nPrint First item in DICT. Secound Item in Set is not possible, \nbecouse we can not have access to Element by index, elemets are random.")
count = 0
for obj in founded.items():
    print(obj)
    count += 1
    if count>0:
        break
print("\nEdit and rePrint DICT. Sets is also not possible edit")
founded["BMW"] = 1916
for key in cars:
    print("SET(DICT Key) --->", key.rjust(12, " "), "\tExist in DICT value {:7}".format(founded[key]))

print("\nSize SETS",len(cars))
print("Size DICT", len(founded))

print("\nSearching SETS and DICT")
schKey = "BMW"
print(schKey, "in Set: ", schKey in cars)
print(schKey, "in Dict(key): ", schKey in founded)

print("\nAdd new elements in SETS and DICT. Reprinted")
cars.add("Tayota")
founded["Tayota"] = 1933
for key in cars:
    print("SET(DICT Key) --->", key.rjust(12, " "), "\tExist in DICT value {:7}".format(founded[key]))

print("\nDiscard of elements")
cars.remove("Tayota")
founded.pop("Tayota")
for key in cars:
    print("SET(DICT Key) --->", key.rjust(12, " ") ,"\tExist in DICT value {:7}".format(founded[key]))

print("Exercise 3 (sum all ell in array)".center(100).upper())
arr = []
for i in range(3):
    arr.append(float(input("insert number :")))
somatório = sum(arr)
print("Sum: ", somatório)


print("Exercise 4 (avarage Number)".center(100).upper())
avarage = somatório/len(arr)
print("Avarage: {:7.2f}".format(avarage))

print("Exercise 5 (Matrix)".center(100).upper())
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
for obj in matriz:
    size = len(obj)-1
    lastPos = sum(obj[:-1])
    obj[size] = lastPos


print("Exercise 6 (Slicing)".center(100).upper())

str = "casI siroB,05"
sl = str.index(",")
name = str[:sl][::-1]
grade = str[sl+1:]
print(name," teve um(a)", grade , " de nota.")

print("Exercise 7 (admins)".center(100).upper())
usr = {"Marta", "David", "Elvira","Juan", "Marcos"}
adm = {"Marta","Juan"}
adm.add("Marcos")
adm.remove("Juan")
for name in usr:
    print(name.ljust(10), "isAdmin: ", name in adm)

print("Exercise 8 (Game)".center(100).upper())

def prnt(obj):
    for key, value in obj.items():
        print("\t", key, " ", value)

cavaleiro = { 'vida':2, 'ataque':2, 'defesa': 2, 'alcance':2 }
guerreiro = { 'vida':2, 'ataque':2, 'defesa': 2, 'alcance':2 }
arqueiro = { 'vida':2, 'ataque':2, 'defesa': 2, 'alcance':2 }

print("cavaleiro".upper())
prnt(cavaleiro)
print("guerreiro".upper())
prnt(guerreiro)
print("arqueiro".upper())
prnt(arqueiro)

print("Level up!!!")
cavaleiro['vida'] = guerreiro['vida'] * 2
cavaleiro['defesa'] = guerreiro['defesa'] * 2
guerreiro['ataque'] = cavaleiro['ataque'] * 2
guerreiro['alcance'] = cavaleiro['alcance'] * 2
arqueiro['vida'] = guerreiro['vida']
arqueiro['ataque'] = guerreiro['ataque']
arqueiro['defesa'] = guerreiro['defesa'] / 2
arqueiro['alcance'] = guerreiro['alcance'] * 2

print("cavaleiro".upper())
prnt(cavaleiro)
print("guerreiro".upper())
prnt(guerreiro)
print("arqueiro".upper())
prnt(arqueiro)
