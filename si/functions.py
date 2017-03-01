import random

mapp = 10

def array_gen():
    lst = []
    for i in range(5):
        lst.append([])
        for y in range(7):
            if random.randrange(0, 6) == 0:
                lst[i].append("*")
            else:
                lst[i].append(" ")

    return lst

