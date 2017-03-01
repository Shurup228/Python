import math as m


eps = 10**-4

x = 1
a = 1

s = 0
while abs(a) <= eps:
    a = 0.5 * (a + 4/a)
    s += a
print(s)