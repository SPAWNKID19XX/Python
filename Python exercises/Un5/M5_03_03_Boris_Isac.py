import json
superherois = {"nomedaEquipa": "Super Hero Squad","cidade": "Metro City","formado": 2016,"baseSecreta": "Super Tower","activo": "Sim","membros": [{"nome": "SuperMan","idade": 29,"identidadeSecreta": "Clart Kent","poderes": ["Super força","Super velocidade","Raio laser"]},{"nome": "Batman","idade": 350,"identidadeSecreta": "Bruce Wayne","poderes": ["Detective","Dinheiro","Raio laser"]},{"nome": "Wonder Woman","idade": 900,"identidadeSecreta": "Diana de Temiscira","poderes": ["Super força","Super velocidade"]}]}
print(type(superherois)) #check type
#change datas
superherois['membros'][0]['poderes'].append('Voar')
superherois["membros"][1]['idade']=35
superherois["membros"][1]['poderes'].remove('Raio laser')
superherois['membros'][2]['poderes'].append('Laço da verdade')
#change type to JSON
superherois = json.dumps(superherois, ensure_ascii=False, indent=4)

print(type(superherois))
print(superherois)