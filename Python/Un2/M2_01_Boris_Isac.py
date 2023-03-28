'''1. Identificamos os tipos de dados (inteiro, float, booleano ou string)
dos seguintes valores'''
"Olá Mundo" #String
True        #Boolean
-25         #Int
1,167       #Float
a =' '      #String

'''2. Indicar o resultado que mostra os prints com base nestas
variáveis (sem necessidade de programar, mentalmente):'''
print("Exercise 2")
a = 10
b = -5
c = "Ola "
print(a * 5)                # 50
print(a - b)                # 15
print(c + "Mundo")          #"Ola Mundo"
print(c * 2)                #"Ola Ola "
print(c[-1])                #" "
print(c[1:])                #"la "

'''3. Armazenar 3 variáveis em 3 strings diferentes, uma das strings deverá ter 50
pontos (.) gerados de uma forma automática.
Criar uma quarta variável que seja a concatenação das 3 strings previamente
criadas, unidos com um travessão "-".
Finalmente imprimir:
a ) esta quarta variável de forma completa
b) mostrando unicamente os 5 primeiros caracteres
c) os 5 últimos caracteres.'''
print("Exercise 3")
a = "."
b = a*50
c = "Hello world!"
d = a+b+c
print("alinha a var a" ,a)
print("alinha b var a" ,a[:5])
print("alinha c var a" ,a[-5:])
print("alinha a var b" ,b)
print("alinha b var b" ,b[:5])
print("alinha c var b" ,b[-5:])
print("alinha a var c" ,c)
print("alinha b var c" ,c[:5])
print("alinha c var c" ,c[-5:])
print("alinha a var d" ,d)
print("alinha b var d" ,d[:5])
print("alinha c var d" ,d[-5:])