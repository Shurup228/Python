
def kyraga(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + kyraga(a, b - 1)

print(kyraga(2, 3))
#dymav xvulun 30