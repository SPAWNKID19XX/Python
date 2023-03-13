import json
str = {"chefe_projeto": {"Nome": "João","Idade": 28,"Experiência": ["Gestão","Finanças","Bases de dados"],"Residência": "Porto","HorasProjeto": 3500},"funcionários": [{"Nome": "Helena","Idade":26,"Experiência":["JavaScript","Python"],"Residência": "Faro","HorasProjeto": 500},{"Nome": "Luis","Idade":31,"Experiência": ["Django","Flask","Pyramid"],"Residência": "Lisboa","HorasProjeto": 1100}]}
print("Class:",type(str), str)

jsonStr = json.dumps(str, ensure_ascii=False, indent=4).encode('utf8')
#Now a size of json file is less, and a script will working quickly
print("Class:",type(jsonStr))
print(jsonStr.decode())