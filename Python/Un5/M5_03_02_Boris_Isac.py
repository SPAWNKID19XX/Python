import json
str = {"chefe_projeto": {"Nome": "João","Idade": 28,"Experiência": ["Gestão","Finanças","Bases de dados"],"Residência": "Porto","HorasProjeto": 3500},"funcionários": [{"Nome": "Helena","Idade":26,"Experiência":["JavaScript","Python"],"Residência": "Faro","HorasProjeto": 500},{"Nome": "Luis","Idade":31,"Experiência": ["Django","Flask","Pyramid"],"Residência": "Lisboa","HorasProjeto": 1100}]}
print("Class:",type(str), str)

jsonStr = json.dumps(str, ensure_ascii=False, indent=4).encode('utf8')
#A resposte - O json é um formato que todas as linguagens de programaçao suportam,
#por isto é bom saber usar. alem disto assim a informaçao pessa mesmo pouco, por
# isto trabalhar com ella vai ser bem mais rapido
print("Class:",type(jsonStr))
print(jsonStr.decode())