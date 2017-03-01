import math as m

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector(Point):
    def __init__(self, Point1, Point2):
        self.x1 = Point1.x
        self.x2 = Point2.x
        self.y1 = Point1.y
        self.y2 = Point2.y
        self.x = Point2.x - Point1.x
        self.y = Point2.y - Point1.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def get_lenght(self):
        return m.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        returnVector = Vector
        returnVector.x = self.x + other.x
        returnVector.y = self.y + other.y
        return returnVector

    def __sub__(self, other):
        returnVector = Vector
        returnVector.x = self.x - other.x
        returnVector.y = self.y - other.y
        return returnVector

p1 = Point(2, 2)
p2 = Point(3, 0)

MyVector = Vector(p1, p2)
print(MyVector)
print(MyVector.get_lenght())
MyVector2 = Vector(p2, p1)
print(MyVector2)
print(Vector.get_lenght(MyVector2 - MyVector))


