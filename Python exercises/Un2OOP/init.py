'''1. Utilizar o método input() para fazer as seguintes tarefas:
• Pedir um número ao utilizador, imprimit o resultado e o seu tipo (para
conhecer em que tipo de dados o input() captura a informação)
• Pedir um número ao utilizador e converter o valor introduzido para o
formato int
• Pedir um número ao utilizador e converter o valor introduzido para o
formato float.
'''
print("Exercicio 1".upper())
inp = input("Intsert a number: ")
print(inp, "-->" ,type(inp))
inp = int(input("Intsert a number: "))
print(inp, "-->" ,type(inp))
inp = float(input("Intsert a number: "))
print(inp, "-->" ,type(inp))

print("Exercicio 2".upper())

'''
2. Formatar os seguintes valores para mostrar o resultado indicado (deve usar o
método format()):
• “Olá Mundo” → Alinhado à direita em 20 caracteres
• “Olá Mundo” → Truncagem no quarto carácter (usar índice 3)
• “Olá Mundo” → Alinhamento ao centro em 20 caracteres com truncagem no segundo carácter (usar índice 1)
• 150 → Formatar com 5 números inteiros preenchidos com zeros
• 7887 → Formatar com 7 números inteiros preenchidos com espaços
• 20.02 → Formatar com 3 números inteiros e 3 números decimais
'''
num1 = 150
num2 = 7887
num3 = 20.02
str="Hello world!!!"
print("Alinhado à direita em 20 caracteres {:>20}".format(str))
print("Truncagem no quarto carácter  {:.3}".format(str))
print("linhamento ao centro em 20 caracteres com truncagem no segundo carácter {:^20.1}".format(str))
print("150 → Formatar com 5 números inteiros preenchidos com zeros:{:05}".format(num1))
print("7887 → Formatar com 7 números inteiros preenchidos com espaços:{:>7}".format(num2))
print("20.02 → Formatar com 3 números inteiros e 3 números decimais:{:07.3f}".format(num3))


