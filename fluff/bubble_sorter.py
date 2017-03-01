# import sys


class bubblesorter:

    def __init__(self, thelist):
        self.mylst = thelist
        self.lenght = len(thelist) - 1


    # def sort(self):
    #     while self.swaps != 0:
    #             if self.count == len(self.unsorted) - 1:
    #                 self.count = 0
    #                 self.swaps = 0
    #
    #             elif self.unsorted[self.count] > self.unsorted[self.count + 1]:
    #                 self.unsorted[self.count], self.unsorted[self.count + 1] = self.unsorted[self.count + 1], self.unsorted[self.count]
    #                 self.count += 1
    #                 self.swaps += 1
    #                 print(self.unsorted)
    #
    #             else:
    #                 self.count += 1
    #                 print(self.unsorted)
    def sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(self.lenght):
                if self.mylst[i] > self.mylst[i + 1]:
                    is_sorted = False
                    self.mylst[i], self.mylst[i + 1] = self.mylst[i + 1], self.mylst[i]
        return self.mylst




mylist123 = [4,5,3,7,9,1,6,7]
print(bubblesorter(mylist123).sort())


