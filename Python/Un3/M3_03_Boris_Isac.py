class Product:
    __id =0
    __name = ""
    __type = "To feed"
    __price = 0.0

    def __init__(self, id, name, type, price):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__price = price
        print(self.__name, "has been created!")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


def __str__(self):
        print("{:<3}{:10}{:10}{:10}".format(self.__id, self.__name, self.__type, self.__price))

#Auto creating of products
idCreator=[1,2,3,4]
nameCreator = ["Apples", "Pants", "Rolex", "Bread"]
typeCreator = ["To Feed", "Cloth", "Watch", "To Feed"]
priceCreator = [1.39, 29.99, 12256, 1.9]
prodList = []

#Create and save list product
for i in range(4):
    prod = Product(idCreator[i], nameCreator[i], typeCreator[i], priceCreator[i])
    prodList.append(prod)

#before changes
print("\nBefore changes")
for obj in prodList:
    obj.__str__()

prodList[1].price = 2.99

#After changes
print("\nAfter changes")
prodList[1].__str__()

print("\nprinting full list after changes!")
for obj in prodList:
    obj.__str__()