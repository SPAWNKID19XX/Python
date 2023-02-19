class Vehicle:
    def __init__(self, color = "White", wheels = 4):
        self.__color = color
        self.__wheels = wheels
        print("Class vehicle has been created")

    def __str__(self):
        return self.__color, self.__wheels

    def setColor(self, value):
        self.__color = value
    def getColor(self):
        return self.__color

    def setWheels(self, value):
        self.__wheels = value
    def getWheels(self):
        return self.__wheels

class Car(Vehicle):
    __brand = ""
    __model = ""
    __spead = 0
    __engine = 1.0

    def setSpeed(self, value):
        self.__spead = value
    def getSpeed(self):
        return self.__spead

    def setEngine(self, value):
        self.__engine = value
    def getEngine(self):
        return self.__engine

    def setBrand(self, value):
        self.__brand = value
    def getBrand(self):
        return self.__brand

    def setModel(self, value):
        self.__model = value
    def getmodel(self):
        return self.__model

    def __rides__(self):
        if self.__spead > 0 and self.__spead <= 50:
            return "Rides slowly, {}km/h".format(self.__spead)
        elif self.__spead > 50:
            return "Rides quiqly, {}km/h".format(self.__spead)
        else:
            return "Stays, {}km/h".format(self.__spead)

    def __str__(self):
        return  """\n
    Brand: {} 
    Model: {}
    Color: {}
    Engine: {}
    NumWheels: {}
    Methode: {}""".format(self.__brand, self.__model, self.getColor(), self.__engine, self.getWheels(), self.__rides__())

carro1 = Car()
carro2 = Car()

print("Before edit Information")
print(carro1.__str__())

print("After edit Information")
carro1.setSpeed(55)
carro1.setBrand("BMW")
carro1.setModel(318)
carro1.setEngine(2.0)
print(carro1.__str__())


carro2.setSpeed(49)
carro2.setBrand("Renault")
carro2.setModel("Clio")
carro2.setEngine(1.3)
carro2.setColor("Black")
print(carro2.__str__())