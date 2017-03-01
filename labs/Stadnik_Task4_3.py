import math as m


epsilon = 10**-4
x = 1
n = float(input("input n"))
a = n

if a < -epsilon:
    print("error")
elif abs(a) < epsilon:
    print(0)
else:
    while abs(a - x) > epsilon:
        a = x
        x = 0.5 * (a + (n / a))
    print(round(x, 4))
