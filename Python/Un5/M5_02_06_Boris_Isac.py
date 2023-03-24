import csv
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
#run csv and append each of column to own list
for i, row in enumerate(readerCsv):
    mpg.append(row[0])
    cylinders.append(row[1])
    displacement.append(row[2])
    horsepower.append(row[3])
    weight.append(row[4])
    acceleration.append(row[5])
    year.append(row[6])
    origin.append(row[7])

#append all lists in main list. will be yeasier to work
fullList.append(mpg)
fullList.append(cylinders)
fullList.append(displacement)
fullList.append(horsepower)
fullList.append(weight)
fullList.append(acceleration)
fullList.append(year)
fullList.append(origin)


#print mainList
for row in fullList:
    print(row)

del readerCsv
file.close()
del file