print("Exercicio 1".upper())
'''
nota1=7
nota2=9
nota3=5
media = (nota1+nota2+nota3)/3
imprimir media
prefero com array
o comentario é so para provar que sei fazer de maneira mais basica
'''
nota = [7,8,9]  #save student's grades
prs = [0.15, 0.35, 0.5]
sum = 0

#Sum up all numbers in arr and save it in var sum
for val in nota:
    sum+=val

mid = sum/len(nota)
print("A nota média é {:02.3}".format(mid))

print("\n\nExercicio 2".upper())
sum = 0
for i in range(3):
    sum += nota[i]*prs[i]
print("A nota média é {:02.3}".format(sum))

print("\n\nExercicio 3".upper())
num1 = float(input("insert num1: "))
num2 = float(input("Insert num2: "))
print("Information about numbers:\n\tSe os dois números são iguais: ",num1==num2, "\n\tSe os dois números são diferentes: " ,num1!=num2, "\n\tSe o primeiro é maior que o segundo: " ,num1 > num2, "\n\tSe o segundo é maior ou igual que o primeiro", num2>=num1)

print("\n\nExercicio 4".upper())
str1 = input("insert string 1: ")
str2 = input("Insert string 2: ")
print(len(str1)>=3 and len(str1)<10)
print(len(str2)>=3 and len(str2)<10)
print((len(str1)>=3 and len(str1)<10) and (len(str2)>=3 and len(str2)<10))

print("\n\nExercicio 5".upper())
numeroMagico = 12345679

numeroUtilizador = int(input("Insert integer number(1..9) : "))
while ((type(numeroUtilizador) != int) or (numeroUtilizador<1) or (numeroUtilizador>9)):
    numeroUtilizador = int(input("Error.Insert integer number(1..9) : "))

numeroUtilizador *= 9
numeroMagico *= numeroUtilizador

print(numeroMagico)