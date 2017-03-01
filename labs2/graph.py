class GraphCore:

    def __init__(self, create_root=False):
        self.relays = {}
        self.points = []
        if create_root: self.create_point('root', 0, 0)

    def create_point(self, name_reference, x, y):
        obj = Point(x, y)
        self.points.append(obj)
        self.relays[str(name_reference)] = [self.points.index(obj)]

    def add_relay(self, point1_reference, point2_reference, both_way=False):
        self.relays[point1_reference].append(point2_reference)
        if both_way:
            self.relays[point2_reference].append(point1_reference)

    def get_all_coords(self):
        for elem in self.points:
            print(elem.get_coordinates())

    def get_point_by_key(self, key):
        return self.points[self.relays[str(key)][0]]


class Point:

    def __init__(self, planar_x, planar_y):
        self.x = planar_x
        self.y = planar_y

    def get_coordinates(self):
        return (self.x, self.y)

def main():

    Core = GraphCore()
    Core.create_point('First', 2, 0)
    Core.create_point('second', 1, 4)
    print(Core.points)
    Core.get_all_coords()
    print(Core.relays.keys())
    print(Core.get_point_by_key('First'))



if __name__ == '__main__':
    main()