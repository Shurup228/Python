from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle(Point):
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def getLinesLength(self):
        line1 = self.getVectorLenght(self.point1, self.point2)
        line2 = self.getVectorLenght(self.point1, self.point3)
        line3 = self.getVectorLenght(self.point3, self.point2)
        return line1, line2, line3

    def getVectorLenght(self, point1, point2):
        return sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

    def getArea(self):
        lengthTup = self.getLinesLength()
        perim = lengthTup[0] + lengthTup[1] + lengthTup[2]
        hper = perim/2
        return sqrt(hper * (hper - lengthTup[0]) * (hper - lengthTup[1]) * (hper - lengthTup[2]))

    def __str__(self):
        area = self.getArea()
        lengthTup = self.getLinesLength()
        return 'Triangle <{}>. Area: {}.\nLine1: {}, Line2: {}, Line3: {}'.format(id(self), area, lengthTup[0],
                                                                                lengthTup[1], lengthTup[2])

if __name__ == '__main__':

    Point1 = Point(3, 0)
    Point2 = Point(4, 2)
    Point3 = Point(0, 2)

    MyTriangle = Triangle(Point1, Point2, Point3)
    print(MyTriangle)