#Python 3.10.8

cores = { 'vermelho':'red', 'verde':'green', 'preto':'black' }

try:
    cores['branco']
except:
    txt = input("branco, não está no dicionario!\nSe queser adicionar, escreva o valor: ")# se for em branco ou numeros, nao sera adicionado
    if (txt != "") and (txt.isalpha()):
        cores["branco"] = txt

print(cores)