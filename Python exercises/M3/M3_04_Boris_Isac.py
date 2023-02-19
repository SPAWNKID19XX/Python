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

    def setId(self, value):
        self.__id = value
    def getId(self):
        return self.__id

    def setName(self, value):
        self.__name = value
    def getName(self):
        return self.__name

    def setType(self, value):
        self.__type = value
    def getType(self):
        return self.__type

    def setPrice(self, value):
        self.__price = value
    def getPrice(self):
        return self.__price

    def __str__(self):
        return  "{:<3}{:10}{:10}{:10}".format(self.__id, self.__name, self.__type, self.__price)

#Auto creating of products
idCreator=[1,2,3,4]
nameCreator = ["Apples", "Pants", "Rolex", "Bread"]
typeCreator = ["To Feed", "Cloth", "Watch", "To Feed"]
priceCreator = [1.39, 29.99, 12256, 1.91]
prodList = []

#Create and save list product
for i in range(4):
    prod = Product(idCreator[i], nameCreator[i], typeCreator[i], priceCreator[i])
    prodList.append(prod)

#before changes
print("\nBefore changes\n{:3}{:10}{:10}{:>10}".format("ID", "Name","Type", "Price"))
for obj in prodList:
    print(obj.__str__())

searchById = int(input("Product ID?: "))
for obj in prodList:
    if obj.getId() == searchById:
        print(obj.__str__())
        quantety = int(input("Haw many pieces do you wont? "))
        priceFinal = quantety * obj.getPrice()
        print("Final price for {} {} is {:3.7}".format(quantety, obj.getName(), priceFinal))