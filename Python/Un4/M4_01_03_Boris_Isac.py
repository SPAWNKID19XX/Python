class Animal:
    def __init__(self,name, age):
        self.myDict = {"name":name, "age":age}

    def speak(self):
        print(self.myDict["name"] , "speaking!")

    def __str__(self):
        for k,v in self.myDict.items():
            print("\t",k , ":" , v)

class WildAnimals(Animal):
    def __init__(self, name, age, eatingMeet):
        super().__init__(name, age)
        self.myDict["eatingMeet"] = eatingMeet

    def speak(self):
        print(self.myDict["name"] , "Making noise!")

class VilageAnimals(Animal):
    def __init__(self, name, age, sleep):
        super().__init__(name, age)
        self.myDict["sleep"] = sleep

class Beards(VilageAnimals):
    def __init__(self, name, age, playing, fly):
        super().__init__(name, age, playing)
        self.myDict["fly"] = fly

    def speak(self):
        print(self.myDict["name"] , "Sings!")

class Pets(VilageAnimals):
    def __init__(self, name, age,sleep, playing):
        super().__init__(name, age, sleep)
        self.myDict["playing"] = playing

    def speak(self):
        print(self.myDict["name"] , "barking!")




leon = Animal("Symba", 3)
print(type(leon).__name__)
leon.__str__()
leon.speak()

elefante = WildAnimals("Jumbo", 5, False)
print(type(elefante).__name__)
elefante.__str__()
elefante.speak()

horse = VilageAnimals("Pony",10, True)
print(type(leon).__name__)
horse.__str__()
horse.speak()

beards = Beards("Beard",1,False,True)
print(type(beards).__name__)
beards.__str__()
beards.speak()

dog = Pets("Rax",12,False, True)
print(type(dog).__name__)
dog.__str__()
dog.speak()