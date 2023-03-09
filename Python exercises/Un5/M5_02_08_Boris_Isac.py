import csv, statistics
file = open("02_CSV_data.csv", "r")
readerCsv = csv.reader(file)
#creating empty list
fullList = []
mpg=[]
cylinders=[]
displacement=[]
horsepower=[]
weight=[]
acceleration=[]
year=[]
origin=[]

def delNameCell(list):
    nameList = []
    for row in list:
        nameList.append(row.pop(0))
    return nameList

def retypeFloat(lista):#function will retype from str to float al elements
    for row in lista:
        for i, ele in enumerate(row):
            row[i] = float(row[i])

#run csv and append each of column to own list
for row in readerCsv:
    mpg.append(row[0])
    cylinders.append(row[1])
    displacement.append(row[2])
    horsepower.append(row[3])
    weight.append(row[4])
    acceleration.append(row[5])
    year.append(row[6])
    origin.append(row[7])

#append all lists to main list
fullList.append(mpg)
fullList.append(cylinders)
fullList.append(displacement)
fullList.append(horsepower)
fullList.append(weight)
fullList.append(acceleration)
fullList.append(year)
fullList.append(origin)

nameList = delNameCell(fullList)
retypeFloat(fullList)


del readerCsv
file.close()
del file
for i, row in enumerate(fullList):
    print("{:15} has {} elements. MinValue:{:>7}, MaxValue:{:>7}, Mean:{:7.5}, Median:{:7.5}, Deviation:{:7.5}".format(nameList[i],len(fullList[i]), min(fullList[i]), max(fullList[i]), statistics.mean(fullList[i]), statistics.median(fullList[i]), statistics.pstdev(fullList[i])))
