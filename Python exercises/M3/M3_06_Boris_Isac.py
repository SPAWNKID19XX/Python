import  math

class Point():
    def __init__(self, x=0, y=0 ):
        self.x = x
        self.y = y

    def __str__(self):
        return (self.x, self.y)

    def quadrante(self):
        if self.x > 0 and self.y > 0:
            return "Quadrante I"
        elif self.x < 0 and self.y > 0:
            return "Quadrante II"
        elif self.x < 0 and self.y < 0:
            return "Quadrante III"
        elif self.x > 0 and self.y < 0:
            return "Quadrante IV"
        else:
            return "Origem"

    def vetor(self, p2x, p2y):
        return p2x-self.x, p2y-self.y

    def distance(self, p2x, p2y):
        return  math.sqrt(((p2x-self.x)**2)+((p2y-self.y)**2))


class Rectangle():
    upLeft = Point()
    rightDown = Point()

    def __init__(self, upLeft, rightDown):
        self.upLeft = upLeft
        self.rightDown = rightDown

    def base(self):
        return self.rightDown.x-self.upLeft.x

    def altura(self):
        return self.rightDown.y - self.upLeft.y

    def area(self):
        return (self.rightDown.x-self.upLeft.x)*(self.rightDown.y - self.upLeft.y)

namePoint = ["A", "B", "C", "D"]
pA = Point(3,2)
pB = Point(5,5)
pC = Point(-3,-1)
pD = Point()

longestPoint = 0
points = [pA, pB, pC, pD]

for i, obj in enumerate(points):
    print(namePoint[i], obj.__str__(), obj.quadrante())

print("\nVector AB: ",pA.vetor(pB.x,pB.y))
print("Vector BA: ",pB.vetor(pA.x,pA.y))
print("\nDistance AB: ", pA.distance(pB.x,pB.y)) #se quesece formatar ponha {:5.2f}
print("Distance BA: ", pB.distance(pA.x,pA.y)) #se quesece formatar ponha {:5.2f}

distancePoints = [pA.distance(0,0), pB.distance(0,0), pC.distance(0,0)]


for i, obj in enumerate(distancePoints):
    if obj > longestPoint:
        longestPoint = distancePoints[i]
        leterPoint = namePoint[i]

print("\nPoint {}  at the farthest distance {}".format(leterPoint, longestPoint))
rect = Rectangle(pA, pB)
print("\nBase: ",rect.base())
print("Altura: ", rect.altura())
print("Area: ",rect.area())
