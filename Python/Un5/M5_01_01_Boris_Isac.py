#python 3.10.8
txt = "Olá, que tal está\nIsto é uma prova\nHoje não chove\nAproxima-se o natal\nAté logo e muito boas"

inputFile = open("provas.txt", "w",encoding="UTF-8")
inputFile.write(txt)
inputFile.close()

inputFile = open("provas.txt", "r", encoding="UTF-8")
lista = inputFile.readlines()
print("Name: " ,inputFile.name, " \nClosed: " ,inputFile.closed, "\nMode: ", inputFile.mode)
inputFile.close()

print(lista)