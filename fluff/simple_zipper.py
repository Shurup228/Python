count = 0


class zipper:
    def __init__(self, count=0, pointer=0):
        self.list = [x for x in range(count)]
        self.pointer = pointer

    def getCurr(self):
        print(self.list[self.pointer])

    def moveNext(self):
        self.pointer += 1

    def movePrev(self):
        self.pointer -= 1

    def moveTo(self, movevar):
        self.pointer += movevar


f = zipper()
