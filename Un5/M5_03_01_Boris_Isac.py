import json
#criamos as esperiencias das pessoas
expJoao = ["Gestão","Finanças","Bases de dados"]
expHelena = ["JavaScript","Python"]
expLuis = ["Django","Flask","Pyramid"]
#criamos os dict de staff
dictJoao = {
    "Nome": "João",
    "Idade": 28,
    "Experiencia": expJoao,
    "Residência": "Porto",
    "HorasProjeto": 3500
}
dictHelena = {
    "Nome": "Helena",
    "Idade": 26,
    "Experiência":expHelena,
    "Residência": "Faro",
    "HorasProjeto": 500
}
dictLuis = {
    "Nome": "Luis",
    "Idade": 31,
    "Experiência": expLuis,
    "Residência": "Lisboa",
    "HorasProjeto": 1100
}
#criamos a lista de funcionarios
listFuncionarios = [dictHelena,dictLuis]
#preenchemos o dicionario com os objetos e listas
str = {
    "chefe_projeto": dictJoao,
    "funcionários": listFuncionarios
}

#str = {"chefe_projeto": {"Nome": "João","Idade": 28,"Experiência": ["Gestão","Finanças","Bases de dados"],"Residência": "Porto","HorasProjeto": 3500},"funcionários": [{"Nome": "Helena","Idade":26,"Experiência":["JavaScript","Python"],"Residência": "Faro","HorasProjeto": 500},{"Nome": "Luis","Idade":31,"Experiência": ["Django","Flask","Pyramid"],"Residência": "Lisboa","HorasProjeto": 1100}]}
print("Class:",type(str), str)
jsonStr = json.dumps(str, ensure_ascii=False, indent=4)
horas_chefe = str['chefe_projeto']['HorasProjeto']

print(jsonStr)
horas_funcionarios = 0
for obj in str['funcionários']:
    horas_funcionarios += obj['HorasProjeto']
print("Horas Chefe:{:>12}\nHoras Funcionarios:{:>5}".format(horas_chefe, horas_funcionarios))