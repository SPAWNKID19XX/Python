'''
print("Exercise 1".rjust(50))
#area of a rectangle, User insert 2 length and function area_retangulo() will return area


def area_retangulo(length, width):
    return length*width

length = int(input("Insert length: "))
width = int(input("Insert width: "))

area = area_retangulo(length,width)
print("Area of a rectangle =",area,"sq")

print("Exercise 2".rjust(50))
#area of a circl, User insert radius and function area_circulo() will return area
import  math

def area_circulo(rad):
    return rad**2*math.pi

rad=int(input("insert a radius of a circle: "))
area = area_circulo(rad)
print("Area of a circle = {:5.2f}".format(area))


print("Exercise 3".rjust(50))
#User insert 2 numbers num1 and num2, function relacao() return 1 if a>b, -1 if a<b, and 0 if a=b
def relacao(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

num1 = int(input("Insert num1: "))
num2 = int(input("Insert num2: "))
print(relacao(num1, num2))

print("Exercise 4".rjust(50))

def lerNumero():#asc to user to insert a num, print it and return it
    num = int(input("Insert a number: "))
    print(num)
    return num

def maior(a):#compair a numbers and assign biggest num to var maior and after that return maior
    maior = a[0]
    for obj in a:
        if obj>maior:
            maior = obj
    return maior

a = []
for i in range(3):
    a.append(lerNumero())

print("maior" , maior(a))
'''
print("Exercise 5".rjust(50))

def imc(w,h):
    imc = w/h**2
    return imc

def printIMC(imc):
    if imc>0 and imc<=18.5:
        return "Baixo peso"
    elif imc>18.5 and imc<=25:
        return "Normal"
    elif imc>25 and imc<30:
        return "Sobrepeso"
    else:
        return "Obesidade"

weight = float(input("Insert your weight(87.5): "))
height = float(input("insert your height(1.87): "))

res = printIMC(imc(weight,height))
print(res)