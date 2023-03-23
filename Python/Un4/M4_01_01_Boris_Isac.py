class Vehicle:
    def __init__(self, brand = "BMW", model = 318):
        self.brand = brand
        self.model = model

    def reabastecer(self):
        return "Este veículo tem que reabastecer gasolina"

    def __str__(self):
        return "{} {}".format(self.brand, self.model)

class VElectric:
    def __init__(self,brand,model, authonomia):
        self.brand = brand
        self.model = model
        self.authonomia = authonomia

    def reabastecer(self):
        return "Este veículo tem que reabastecer a eletricidade"

    def __str__(self):
        return "{} {} {}".format(self.brand, self.model, self.authonomia)

class BicicletaEletrica(VElectric,Vehicle):
    pass

class Quadraciclo(Vehicle, VElectric):
    pass


bmw = Vehicle()
print(bmw)
print(bmw.reabastecer())

tesla = VElectric("tesla",550,45)
print(tesla)
print(tesla.reabastecer())

jansno = VElectric("JANSNO", "X50", 35)
print(jansno)
print(jansno.reabastecer())

quadraciclo = Quadraciclo("CFFOrce", "520L")
print(quadraciclo)
print(quadraciclo.reabastecer())
#print(BicicletaEletrica.mro())
#print(Quadraciclo.mro())
