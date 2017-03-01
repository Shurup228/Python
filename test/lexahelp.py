
def Summ(n, y):
    if not y:
        return n
    else:
        n += 1
        return Summ(n, y-1)



print(Summ(4, 5))
