

class Zipper:
    def __init__(self, lst, count = 0):
        self.count = count
        self.list = lst

    def next(self):
        self.count += 1

    def prev(self):
        self.count -= 1

    def __call__(self, *args):
        if args:
            self.list[self.count] = args[0]
        else:
            return self.list[self.count]


class Zipper2(Zipper):
    def __init__(self, lst, count = 0):
        super().__init__(lst, count = 0)
        self.len = len(self.list)

    def __call__(self, *args):
        if args:
            self.list[self.count], self.list[self.count + 1] = args[0], args[1]
        else:
            return self.list[self.count], self.list[self.count + 1]

    def __next__(self):
        if self.count + 1 == self.len:
            self.count = 0
            raise StopIteration
        else:
            super().next()
            return self.list[self.count - 1], self.list[self.count]

    def __iter__(self):
        return self

    def swap(self):
        self.list[self.count - 1], self.list[self.count] = self.list[self.count], self.list[self.count - 1]

    def prev(self):
        if self.count - 1 == 0:
            pass
        else:
            super().prev()

    def set_count(self, x = 0):
        self.count = x


def bubblesort(lst1):
    lst1 = Zipper2(lst1)
    repeat = 0
    while repeat >= 0:
        # a,b = lst1()
        # if a > b:
        #     lst1.swap()
        #     lst1.next()
        # else:
        #     lst1.next()
        print("in while")
        for a,b in lst1:
            print("in for",a,b,lst1.count)

            if a > b:
                lst1.swap()
                repeat += 1
                print('swapping, repeat + 1', repeat)
            else:
                print('not swapping', repeat)
        repeat -= 1
        print(lst1.list)

    return lst1.list


# z = [3,5,1,2,6]