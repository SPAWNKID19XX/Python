class Vehicle:#create class Vehicle
    lista = []
    def __init__(self, color = "Black", wheels = 4):#initialization
        self.color = color
        self.wheels = wheels

    def __str__(self): #format Print
        return "{}".format(self.__dict__)

    def filtrar(self,nameClass, lista = []):
        listaCarros = []
        for obj in lista:
            if type(obj).__name__ == nameClass:
                listaCarros.append(obj)
        return listaCarros




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
a1 = Vehicle()
a2 = Vehicle()
b = Car()
b1 = Car()
c = Tier()
c1 = Tier()
c2 = Tier()
d = Bike()
e = Moto()
e1 = Moto()
e2 = Moto()
vehicoleInstances = [a,a1,a2,b,b1,c,c1,c2,d,e,e1,e2]

vehicle = []
for obj in vehicoleInstances:
    vehicle.append(obj)

listaCarros = a.filtrar("Moto",vehicle)

for obj in listaCarros:
    print(obj)


