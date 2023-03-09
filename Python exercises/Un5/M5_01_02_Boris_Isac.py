inputFile = open("provas.txt", "r", encoding="UTF-8")
print("Leitura de uma linha: ",inputFile.readline())
print("Leitura de linha a Linha:\n",inputFile.read())
inputFile.close()
