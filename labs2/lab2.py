import random as rand

lst = []

iter = 0
while iter != 10:
    lst.append(rand.randrange(1, 10))
    iter += 1

lst2 = []


lst.sort(), lst2.sort(), print(lst, lst2)