import datetime

months = ("January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December")

def formatoData(data, mes = []):
    print("{} de {} de {}".format(data.day, mes[data.month-1], data.year))

formatoData(datetime.datetime(1987,8,6), months)

formatoData(datetime.datetime.now(), months)