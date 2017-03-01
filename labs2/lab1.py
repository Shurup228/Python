#lab1, varian 6
import random


lst = []
list_lenght = int(input("Input your list lenght\n"))

iter_count = 0
while iter_count < list_lenght:
    lst.append(int(random.randrange(1, 10)))
    iter_count += 1

print(lst)

lst2 = []

def checkForElem(par_var, par_lst):
    for elem in par_lst:
        if elem == par_var:
            return True
    return False

for elem in lst:
    if checkForElem(elem, lst2) == False:
        lst2.append(elem)
lst2.sort()
print(lst2)





