def collatz(number):
    if number%2 ==0:
        print(number/2)
    else:
        print(3*number+1)
    return number

res = 0
num = int(input('insert a number: '))
collatz(num)
print(collatz(num))