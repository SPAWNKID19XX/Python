#python 3.10.8
elementos = [1, 5, -2]

def agrigarUmaVez(val, lista = []):
    if val in lista:
        print('"Erro: impossível adicionar elementos duplicados =>', val)
    else:
        lista.append(val)

agrigarUmaVez(10,elementos)
agrigarUmaVez(-2, elementos)
agrigarUmaVez("Ola", elementos)

print(elementos)