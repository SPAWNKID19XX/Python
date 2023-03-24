#python 3.10.8
def printPessoas(arr = []):
    for obj in arr:
        print("(id={}) {} {} => {}".format(obj["id"], obj["nome"], obj["apelido"], obj["nascimento"]))


pessoas = []

file = open("pessoas.txt", "r", encoding="UTF-8")
for obj in file.readlines():
    myDict = {"id": 0, "nome": "", "apelido": "", "nascimento": ""}
    datas = obj.split(";")
    myDict["id"] = datas[0]
    myDict["nome"] = datas[1]
    myDict["apelido"] = datas[2]
    myDict["nascimento"] = datas[3]
    pessoas.append(myDict)

print("Monstrar a lista".upper())
printPessoas(pessoas)


