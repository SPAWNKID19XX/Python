class Vehicle:
    def __init__(self, color = "White", wheels = 4):
        self.__color = color
        self.__wheels = wheels
        print("Class vehicle has been created")

    def __str__(self):
        return self.__color, self.__wheels

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def wheels(self):
        return self.__wheels
    @wheels.setter
    def wheels(self, value):
        self.__wheels = value

class Car(Vehicle):
    __brand = ""
    __model = ""
    __spead = 0
    __engine = 1.0

    @property
    def speed(self):
        return self.__spead
    @speed.setter
    def speed(self, value):
        self.__spead = value

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, value):
        self.__engine = value

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, value):
        self.__model = value


    def __rides__(self):
        if self.__spead > 0 and self.__spead <= 50:
            return "Rides slowly, {}km/h".format(self.__spead)
        elif self.__spead > 50:
            return "Rides quiqly, {}km/h".format(self.__spead)
        else:
            return "Stays, {}km/h".format(self.__spead)

    def __str__(self):
        return  """
    Brand: {} 
    Model: {}
    Color: {}
    Engine: {}
    NumWheels: {}
    Methode: {}""".format(self.__brand, self.__model, self.color, self.__engine, self.wheels, self.__rides__())

carro1 = Car()
carro2 = Car()

print("Before edit Information")
print(carro1.__str__())

print("After edit Information")
carro1.speed = 55
carro1.brand = "BMW"
carro1.model = 318
carro1.engine = 2.0
print(carro1.__str__())


carro2.speed = 49
carro2.brand ="Renault"
carro2.model ="Clio"
carro2.engine = 1.3
carro2.color = "Black"
print(carro2.__str__())