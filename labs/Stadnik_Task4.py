




epsilon = 10**-4

n = 0
sum = 0
while abs(1 / 2 ** n) + (1 / 3 ** n) >= epsilon:
    sum += (1 / 2 ** n) + (1 / 3 ** n)
    print((1 / 2 ** n) + (1 / 3 ** n))
    n += 1

# Используем цикл для вычисления суммы ряда

print("sum = %s, next_val=%s" % (sum, (1 / 2 ** n) + (1 / 3 ** n)))


# % - оператор форматирования строки

def countt(n):
    digits = 0
    if abs(n) <= epsilon:
        digits = 1
        return "num of digits = ", digits
    else:
        while abs(n) > 1:
            n /= 10
            digits += 1
        return "num of digits = ", digits

# создаем функцию countt принимающую 1 аргумент
# в данном случае мы используем не return а print()

print(countt(5))

# вызываем ту же функцию для нужного нам числа



