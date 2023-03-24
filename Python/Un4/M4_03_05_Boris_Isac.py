#python 3.10.8
elementos = [1, 5, -2]

def agrigarUmaVez(val, lista = []):
    try:
        if val in lista:
            raise ValueError ('Error: impossível adicionar elementos duplicados =>', val)
        else:
            lista.append(val)
    except:
        print('EXCEPTION***Error: impossível adicionar elementos duplicados =>', val)

agrigarUmaVez(10,elementos)
agrigarUmaVez(-2, elementos)
agrigarUmaVez("Ola", elementos)

print(elementos)