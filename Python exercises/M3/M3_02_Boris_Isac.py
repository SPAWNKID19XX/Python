from typing import Any


class Aluno:
    def __init__(self,nome,nota ):
        self.__nome = nome
        self.__nota = nota
#Getters and Setters
    @property
    def infoNome(self):
        return  self.__nome
    @infoNome.setter
    def infoNome(self,nome):
        self.__nome = nome

    @property
    def infoNota(self):
        return self.__nota
    @infoNota.setter
    def infoNota(self, nota):
        self.__nota = nota
#Finish Getters and setters

person = Aluno("Boris", 10)
personEmily = Aluno("Emily", 20)
print(person.infoNome, person.infoNota)
person.infoNome = "Aaron"
person.infoNota = 15
print(person.infoNome, person.infoNota)
print(personEmily.infoNome, personEmily.infoNota)


person.__nome#Error var private