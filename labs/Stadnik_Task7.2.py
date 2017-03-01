import math
fact = math.factorial


def catalan(n):
    n += 1
    lst = [elem for elem in range(n)]
    print(lst)
    for elem in lst:
        print("elem", elem)
        lst[elem] = int(fact(2*elem) / (fact(elem) * fact(elem + 1)))
    del lst[0]
    print(lst)

catalan(3)

