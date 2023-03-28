import  datetime

dTime = datetime.datetime.now()

print(dTime.strftime("Dia: %d\nMes: %m\nAno: %Y\nHora: %H\nMinutos: %m\nSegundos (e milissegundos): %S,%f"))