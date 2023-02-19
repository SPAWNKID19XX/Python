from typing import Any


class Aluno:
    def __init__(self,nome,nota ):
        self.__nome = nome
        self.__nota = nota

    def getInfo(self):
        print(self.__nome, self.__nota)

    def setInfo(self):
        nome = input("insere o nome:")
        nota = input("Insere a nota: ")
        self.__nome = nome
        self.__nota = nota

b = Aluno("Boris", 10)
b.getInfo()
b.setInfo()
b.getInfo()
b.nome#Error var private