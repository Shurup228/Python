from math import sqrt, pi


class Circle:
    def __init__(self, radius, x, y):
        self.r = radius
        self.x = x
        self.y = y

    def __str__(self):
        return '''Circle <{}>, Area: {}, Length: {}, Diameter: {}, Center at: ({}, {})'''.format(id(self),
                                                                                                 self.getArea(),
                                                                                                 self.getLength(),
                                                                                                 self.getDiameter(),
                                                                                                 self.x,
                                                                                                 self.y)

    def getArea(self):
        return pi * self.r**2

    def getLength(self):
        return 2 * pi * self.r

    def getDiameter(self):
        return self.r * 2

    def getSectorArea(self, angle):
        return (pi * self.r ** 2 * angle) / 360

    def getLineLenght(self, angle):
        return (pi * self.r * angle) / 180

    def isIntersecting(self, other):
        dist = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if self.r + other.r < dist:
            return False
        else:
            return True

if __name__ ==  '__main__':
    c1 = Circle(3, 0, 0)
    c2 = Circle(3, 10, 10)
    print(c1)

