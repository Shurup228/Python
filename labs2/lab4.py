

class PriorityQueue:
    def __init__(self, lst=[]):
        self.init_lst = lst
        self.queue_lst = []
        self.make_queue()

    def make_queue(self):
        self.queue_lst = self.init_lst

    def add_to_queue(self, item):
        self.queue_lst.append(item)

    def remove_from_queue(self, index=0):
        return self.queue_lst.pop(index)

    def get_priority(self, item):
        priority = 1
        for elem in self.queue_lst:
            if elem > item:
                priority += 1
        return priority

    def pop_highest_priority(self):
        for elem in self.queue_lst:
            if self.get_priority(elem) == 1:
                return self.remove_from_queue(self.queue_lst.index(elem))

    def __str__(self):
        return self.queue_lst


obj = PriorityQueue()
obj.add_to_queue(5)
obj.add_to_queue(4)
print(obj.queue_lst, obj.get_priority(4), "\n", obj.pop_highest_priority())


