
'''
print("Exercise 1".center(50))
Exercise 5
#User insert 3 numbers and script return if sorted ASC or not
#If first number == 0, User should be informed than is  not aloud!

num = 0
nums =[]
for i in range(3):
    if i == 0:
        while num == 0:
            num = int(input("Insert number dif 0: "))
    else:
        num = int(input("Insert number: "))
    nums.append(num)

if (nums[0] < nums[1]) and (nums[1] < nums[2]):
    print("ASC")
else:
    print("Not ASC")


print("Exercise 2".center(50))
#User insert N numbers and script should sum this numbers from 0 until N-1
N = int(input("Insert N: "))
sum = 0
for i in range(N):
    sum += i
    if (int(i) < (N-1)):
        print(i, end = "+")
    else:
        print(i, end = " = ")
        print(sum)


print("Exercise 3".center(50))
#Menu. User insert 2 numbers and will see menu list
#nao entendi bem para que pedir 3 numeros se o programma esta a trabalhar so com 2.
#Na universidade levei pontos a menos porque criei uma variavel que nao utilizei.
menu = {1: "Plus", 2: "Minus", 3: "Multiply"}
num1 = int(input("Insert num 1: "))
num2 = int(input("insert num 2: "))
for key, value in menu.items():
    print(key, "-"*3 ,value)
readMenu = int(input("Change menu: "))
if readMenu == 1:
    print("sum = ",num1+num2)
elif readMenu == 2:
    print("Subtraction = ", num1 - num2)
elif readMenu == 3:
    print("Multiply = ", num1 * num2)
else:
    print("Inserted number doesn\'t exist in menu")

print("Exercise 4".center(50))
#Insert string and script will count all letter "a"
counter = 0
while str != ".":
    str = input("Insert a string: ")
    for l in str:
        if l == "a" or l == "A":
            counter += 1
    print("a = ", counter)

print("Exercise 5".center(50))
#Script working until user insert odd number
num = 1
while (num % 2) != 0:
    num = int(input("Insert Odd number: "))

print("Exercise 6".center(50))
sum = 0
#sum all even numbers between 0..100
for i in  range(0,100,2):
    sum += i
print("Sum even numbers between 0 and 100: ",sum)

print("Exercise 7".center(50))
sum = 0
arr = []
N = int(input("how many numbers do you want to enter: "))
for i in range(N):
    arr.append(int(input("insert a int number: ")))
#aqui eu poderia retirar a linha a seguir e fazer mais 1 for,
# mas isto implicava o tempo de de execuçao de script
    sum += arr[i]
print("Average: {:5.2f}".format(sum/N))
'''
print("Exercise 8".center(50))
#Insert a numbers between 0..9. it could repeat antil number insertet out of range
#Ever a number is repeted, script should print True or False if not repited
set = {1,3,6,9}
num = -1
while num < 0 or num > 9:
    num = int(input("insert number: "))
else:

    if num in set:
        print(num, " in set: ", num in set)
    else:
        print(num, " in set: ", num in set)
'''
print("Exercise 9".center(50))
list = []
for i in range(11):
    list.append(i)
print("Todos os números do 0 ao 10: ", list)
list.clear()

for i in  range(-10, 1):
    list.append(i)
print("Todos os números do -10 ao 0: ", list)
list.clear()

for i in range(0,21,2):
    list.append(i)
print("Todos os números pares do 0 ao 20: ", list)
list.clear()

for i in range(-19,0,2):
    list.append(i)
print("Todos os números ímpares entre -20 e 0: ", list)
list.clear()

for i in range(0,51,5):
    list.append(i)
print("Todos os números múltiplos de 5 do 0 ao 50: ", list)

print("Exercise 10".center(50))
#Concatinate 2 strings without repeats chars
str1 = "Ola mundo"
str2 = "Ola lua"
res = []
for i in str1:
    if i in str2 and i not in res:
        res.append(i)
print(res)


'''
