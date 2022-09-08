import random

myRand =[]
sortRand = []

#insert one million random numbers in array
for i in range(5):
    num = random.randint(1,25)
    myRand.append(num)
print(myRand)

#Sort array

for j in range(len(myRand) - 1):
    if myRand[j] < myRand[j +1]:
        minNum = myRand[j]
        sortRand.append(minNum)
    else:
        minNum = myRand[j +1]
        sortRand.append(minNum)

print(sortRand)