#Python 3.10.8

lista = [1,2,3,4,5]

try:
    print(lista[10]) #list index out of range
except:
    print("Index fora de comprimento da lista. \nIntroduza o index entre 0 e", len(lista)-1)
