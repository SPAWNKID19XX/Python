import datetime

months = ("January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December")

def formatoData(data):
    print(data.strftime("%d de %B de %Y"))

formatoData(datetime.datetime(1987,8,6))

formatoData(datetime.datetime.now())