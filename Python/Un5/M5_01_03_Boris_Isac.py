myTxt = "\nBoris Isac"

file = open("provas.txt", "a", encoding="UTF-8")
file.write(myTxt)
file.close()
file = open("provas.txt", "r", encoding="UTF-8")
print(file.read())
file.close()