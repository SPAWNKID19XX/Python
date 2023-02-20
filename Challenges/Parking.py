import random
"""Class Vehicle will set and get All information about a Car.
Vehicles contain Atributs ---> name, idLicence, handiCap(isHandiCap?), moto(isMoto?:Moto:Car), vip(isVip), plate,enterDate, exitDate
Vehicles contain Methods ---> Getters and Setters for atributes, spandTime(exitTime-enterTime), totalPrice(spendTime*value(value depen of pricelist))

"""
class Vehicle:
    #Initialization
    def __init__(self, name = "", idLicence = 0, plate = "",enterDate = 0, exitDate = 1, price = 0.07,vip = False, moto = False, handiCap = False ):
        self.name = name
        self.idLicence = idLicence
        self.plate = plate
        self.enterDate = enterDate
        self.exitDate = exitDate
        self.price = price
        self.vip = vip
        self.moto = moto
        self.handiCap = handiCap

#Atrebutes's Getters and Setters
    @property
    def infoName(self):
        return self.name
    @infoName.setter
    def infoName(self, value):
        self.name = value

    @property
    def infoIdLicence(self):
        return self.idLicence
    @infoIdLicence.setter
    def infoIdLicence(self, value):
        self.idLicence = value

    @property
    def infoIsHandicap(self):
        return self.handiCap
    @infoIsHandicap.setter
    def infoIsHandicap(self, value):
        self.handiCap = value

    @property
    def infoIsMoto(self):
        return self.moto
    @infoIsMoto.setter
    def infoIsMoto(self, value):
        self.moto = value

    @property
    def infoIsVip(self):
        return self.vip
    @infoIsVip.setter
    def infoIsVip(self, value):
        self.vip = value

    @property
    def infoPlate(self):
        return self.plate
    @infoPlate.setter
    def infoPlate(self, value):
        self.plate = value

    @property
    def infoEnterDate(self):
        return self.enterDate
    @infoEnterDate.setter
    def infoEnterDate(self, value):
        self.enterDate = value

    @property
    def infoExitData(self):
        return self.exitDate
    @infoExitData.setter
    def infoExitData(self, value):
        self.exitDate = value

    @property
    def infoPrice(self):
        return self.price
    @infoPrice.setter
    def infoPrice(self, value):
        self.price = value
#finish Atributes's Getters and Setters

    def __str__(self):#toString
        return "{:15} {:07d} {:7} {:2} {:2} {:2} {:5} {:5} {:5}€/min".format(self.name, self.idLicence,self.plate, self.vip, self.moto, self.handiCap, self.enterDate, self.exitDate, self.price)

#---spandTime count = (exitTime-enterTime)
    def spandTime(self):
        return self.exitDate-self.enterDate

#---TotalPrice=spandtime*value depending if isMoto, isVip, isHandiCap
    def totalPrice(self):
        if self.vip == True: #Vip
            return self.spandTime() * self.price

        if self.moto == True: #Moto
            if self.spandTime() >= 180:
                return (self.spandTime() * self.price) * 2
            else:
                return self.spandTime() * self.price

        if self.handiCap == True: #handiCap
            if self.spandTime() >= 180:
                return (self.spandTime() * self.price) * 2
            else:
                return self.spandTime() * self.price

        if ((self.vip==False) and (self.moto == False) and (self.handiCap == False)):
            if self.spandTime() >= 180:
                return (self.spandTime() * self.price) * 2
            else:
                return self.spandTime() * self.price

class VipCostomers(Vehicle): #Vip Cars
    def __init__(self, name, idLicence, plate,enterDate, exitDate, price = 0.13,vip = True, moto = False, handiCap = False ):
        super().__init__(name,idLicence,plate,enterDate,exitDate)
        self.vip = vip
        self.handiCap = handiCap
        self.moto = moto
        self.price = price

class HandiCapCostomers(Vehicle): #HandiCap
    def __init__(self, name, idLicence, plate, enterDate, exitDate, price=0.10, vip=False, moto=False,handiCap=True):
        super().__init__(name, idLicence, plate, enterDate, exitDate)
        self.vip = vip
        self.handiCap = handiCap
        self.moto = moto
        self.price = price

class MotoCostomers(Vehicle): #moto
    def __init__(self, name, idLicence, plate,enterDate, exitDate, price = 0.05,vip = True, moto = False, handiCap = False ):
        super().__init__(name,idLicence,plate,enterDate,exitDate)
        self.vip = vip
        self.handiCap = handiCap
        self.moto = moto
        self.price = price

def randField():
    isFree = random.getrandbits(1)
    return isFree

def createRandomUser(): #function for emulate ParkingCostumers
    # Create random datas about costomer
    plts = ["11-aa-11", "22-aa-22", "33-aa-33", "44-aa-44", "55-aa-55"]
    surnames = ["Isac", "Iriciuc", "Cimpoies"]
    names = ["Aaron", "Emily", "Boris", "Natasha"]
    name = random.choice(surnames) + random.choice(names)
    id = random.randint(0, 10000)
    plt = random.choice(plts)
    entDate = random.randint(0, 50)
    exDate = random.randint(50, 250)
    return name,id,plt,entDate,exDate

floor = [] #5 floors

freeForFloor = [] #conter free places[simpleCar, Moto, Vip, HandiCap]

for flr in range(5):
    freePlaces = [0, 0, 0, 0]  # conter free places[simpleCar, Moto, Vip, HandiCap]
    for plc in range(25): #Appending carrs
        places = []  # 40 places for a flor 25simpleCars, 10Moto, 3Vip, 2HandiCap
        a = randField()
        if a == 1:
            castomer = Vehicle(createRandomUser()[0], createRandomUser()[1], createRandomUser()[2],createRandomUser()[3], createRandomUser()[4])
            places.append(castomer)
        else:
            places.append(0)
            freePlaces[0] += 1

    for plc in range(10):#Appending Moto
        a = randField()
        if a == 1:
            costomer = MotoCostomers(createRandomUser()[0], createRandomUser()[1], createRandomUser()[2],createRandomUser()[3], createRandomUser()[4])
            places.append(costomer)
        else:
            places.append(0)
            freePlaces[1] += 1
    for plc in range(3):#Appending Vip
        a = randField()
        if a == 1:
            costomer = VipCostomers(createRandomUser()[0], createRandomUser()[1], createRandomUser()[2],createRandomUser()[3], createRandomUser()[4])
            places.append(costomer)
        else:
            places.append(0)
            freePlaces[2] += 1
    for plc in range(2):  # Appending HandiCap
        a = randField()
        if a == 1:
            costomer = HandiCapCostomers(createRandomUser()[0], createRandomUser()[1], createRandomUser()[2],createRandomUser()[3], createRandomUser()[4])
            places.append(costomer)
        else:
            places.append(0)
            freePlaces[3] += 1
    floor.append(places)
    freeForFloor.append(freePlaces)

print("Parking has been emulated!")
for flr in floor:
    for obj in flr:
        if obj != 0:
            print("{} TotalPrice:{:5.3}€".format(obj, obj.totalPrice()))



#printing free plases information
print("{:20}{:10}{:10}{:10}{:10}".format("Empty places:", "Car", "Moto", "Vip", "HCap"))
for i,floor in enumerate(freeForFloor):
    print("Floor {:6}{:10}{:10}{:10}{:10}".format(i, freeForFloor[i][0],freeForFloor[i][1],freeForFloor[i][2], freeForFloor[i][3]))