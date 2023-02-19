class Vehicle:
    listCatalog = []
    def __init__(self, color = "Black", wheels = 4):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "{}".format(self.__dict__)


class Car(Vehicle):
    def __init__(self, spead = 0, engine = 1.0):
        super().__init__()
        self.spead = spead
        self.engine = engine

class Tier(Car):
    def __init__(self, cargo = 0):
        super().__init__()
        self.wheels = 10
        self.cargo = cargo

class Bike(Vehicle):
    def __init__(self, type = "Urbane"):
        super().__init__()
        self.wheels = 2
        self.type = type

class Moto(Bike):
    def __init__(self, spead = 0, engine = 1.0):
        super().__init__()
        self.spead = spead
        self.engine = engine

def catallog(lokingForNumWheels ,listCatalog = []):
    counter = 0
    for obj in listCatalog:
        if obj.wheels == lokingForNumWheels:
            counter += 1
            print(type(obj).__name__, "\n\t", obj.wheels)
    if counter == 0:
        print(f"Do not exist instance with {lokingForNumWheels} wheels")
    else:
        print(f"Encontrou-se {counter} veículos com {lokingForNumWheels} rodas")

a = Vehicle()
b = Car()
c = Tier()
d = Bike()
e = Moto()
vehicoleInstances = [a,b,c,d,e]

vehicle = []
for obj in vehicoleInstances:
    vehicle.append(obj)

catallog(0 ,vehicle)
catallog(2 ,vehicle)
catallog(4 ,vehicle)
