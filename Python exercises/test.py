class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        print(self.name, self.age)

class Teacher(Person):
    def __init__(self, name, age, prof = "Teacher"):
        super().__init__(name, age)
        self.prof = prof

    def __str__(self):
        print(self.name, self.age, self.prof)

person = Person("Boris", 35)
person.__str__()
teacher = Teacher("Aaron", 10)
teacher.__str__()