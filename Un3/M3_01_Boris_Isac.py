class Aluno:
    nome = ""
    nota = 0
    def __init__(self, name, nota):
        self.name = name
        self.nota = nota
        print("O aluno {} foi criado com sucesso".format(self.name))

    def __str__(self):
        print("{} {}".format(self.name, self.nota))

    def qualificacao(self):
        qualif = "Reprovado"
        if self.nota >= 9.5:
            qualif = "Aprovado"
            print(self.name, self.nota, qualif)
        else:
            print(self.name, self.nota, qualif)

Boris = Aluno("Boris", 8)#criaçao
Boris.__str__()#method __string__
Boris.qualificacao()#method qualificacao
Aaron = Aluno("Aaron", 9.5)#criaçao
Aaron.__str__()#method __string__
Aaron.qualificacao()#method qualificacao
Emily = Aluno("Emily", 11)#criaçao
Emily.__str__()#method __string__
Emily.qualificacao()#method qualificacao
Natasha = Aluno("Natasha", 15)#criaçao
Natasha.__str__()#method __string__
Natasha.qualificacao()#method qualificacao