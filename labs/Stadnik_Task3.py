import math

print("Intro to programming Task3")
print("Stadnik Andriy, FF-61-115")
x = float(input("Input x: "))
y = float(input("Input y: "))

epsilon = 10**-4



if x**3-y**3 <= epsilon or x<0:
    print("error")
z=((1/(x**3-y**3))-math.sqrt(2*x))
print(z)


# Тут мы проверяем введенные значения, что бы они соответствовали области допустимых значений выражения
# В данном случае это неотрицательность числа под корнем и неравность знаменателя нулю
# math.sqrt - функция извлечения корня (функция импортирована из модуля math)