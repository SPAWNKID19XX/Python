file = open("provas.txt", "w", encoding="UTF-8")
file.write("Portugal")
file.close()

file=open("provas.txt", "r", encoding="UTF-8")
print(file.read())
file.close()