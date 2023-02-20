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
            self.__finalPrice += obj.price * self.quantetyList[i]
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
invoice.__mostrar_pedido__()
print("Final price: {:10.2f} €".format(invoice.__total_pedido__()))

