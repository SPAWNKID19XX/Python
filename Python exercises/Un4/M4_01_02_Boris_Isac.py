class Pessoal_Universitario:
    def __init__(self, id, name, mail):
        self.myDict = {"id": id, "name": name, "mail": mail}

    def __str__(self):
        for k,v in self.myDict.items():
            print("\t",k , ":" , v)

class Escritorio(Pessoal_Universitario):
    def __init__(self, id, name, mail, gabinete):
        super().__init__(id, name, mail)
        self.myDict["gabinete"] = gabinete

class Professor(Pessoal_Universitario):
    def __init__(self, id, name, mail, especializacao):
        super().__init__(id, name, mail)
        self.myDict["especializacao"] = especializacao


class Aluno(Pessoal_Universitario):
    def __init__(self, id, name, mail, creditosAprovados):
        super().__init__(id, name, mail)
        self.myDict["creditosAprovados"] = creditosAprovados

pessoa = Pessoal_Universitario(1,"Boris","boris@test.com")
escritorio = Escritorio(2,"Emily","emily@test.com",5)
prof = Professor(3,"Aaron","Aaron@test.com", "Bazes de programaçao")
aluno = Aluno(4,"Natasha","natasha@test.com", 3)

print(type(pessoa).__name__)
pessoa.__str__()
print(type(escritorio).__name__)
escritorio.__str__()
print(type(prof).__name__)
prof.__str__()
print(type(aluno).__name__)
aluno.__str__()