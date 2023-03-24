#Python 3.10.8

lista = [1,2,3,4,5]

try:
    print(lista[10]) #list index out of range
except IndexError:
    print("IndexError: list index out of range\nIntroduza o index entre 0 e", len(lista)-1)
