class Product:
    __id =0
    __name = ""
    __type = "To feed"
    __price = 0.0

    def __init__(self, id = None, name = None, type = None, price = None):
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

class Order:
    orderList = []
    quantetyList = []
    __finalPrice = 0

    def __init__(self, orderList = [], quantetyList = []):
        self.orderList = orderList
        self.quantetyList = quantetyList
        print("Class Order has been created")

    def  __mostrar_pedido__(self,orderList = [], quantetyList = []):
        print("{:<3}{:10}{:15}{:10}{:10}".format("ID", "NAME", "TYPE", "PRICE", "QUANTETY"))
        for i, obj in enumerate(self.orderList):
            print("{}{:10}".format(obj, self.quantetyList[i]))

    def  __total_pedido__ (self):
        for i, obj in enumerate(self.orderList):
            self.__finalPrice += obj.getPrice() * self.quantetyList[i]
        return self.__finalPrice

#Auto creating of products
idCreator=[1,2,3,4]
nameCreator = ["Apples", "Pants", "Rolex", "Bread"]
typeCreator = ["To Feed", "Cloth", "Watch", "To Feed"]
priceCreator = [1.39, 29.99, 12256, 1.91]
fullOrderList = []
prodList = []
quantetyList = []


#Create and save list product
for i in range(4):
    prod = Product(idCreator[i], nameCreator[i], typeCreator[i], priceCreator[i])
    prodList.append(prod)
    res = int(input("Add to cart? (1-yes / 0-no): "))
    if res == 1:
        fullOrderList.append(prod)
        quantetyList.append(int(input("Haw many?: ")))


invoice = Order(fullOrderList, quantetyList)
print("\nInvice nº 0")
invoice.__mostrar_pedido__()
print("Final price: {:10.2f} €".format(invoice.__total_pedido__()))

