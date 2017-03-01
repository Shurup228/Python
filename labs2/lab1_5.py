print("vvedit' promijok [a;b)")
input_a = int(input("vvedit' a"))
input_b = int(input("vvedit' b"))

lst = [x for x in range(input_a, input_b)]

print(lst)


def shift(l, n):
    return l[(-n):] + l[:(-n)]

print(shift(lst, 0))
