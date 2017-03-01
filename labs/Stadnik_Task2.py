#Intro to programming Task2, Stadnik Andriy, FF-61-115
print("Intro to programming Task2")
print("Stadnik Andriy, FF-61-115")


# Все те же выводы с помощью print()


x = float(input('Input x: '))
y = float(input('Input y: '))
z = float(input('Input z: '))

# Функция input() позволяет ввести данные с клавиатуры
# Аргументом будет строка которая будет выведена перед ожиданием ввода
# Так как данные введенные с помощью input() являются "string" (строковый литерал),
# мы используем функцию float, что бы привести наши данные к числу с плавающей точкой

epsilon = 10**-4

# epsilon, наш "условный ноль". Что бы понять необходимость этого числа, необходимо знать что такое
# "машинный ноль" и "машинное эпсилон"

if abs(y-21.1)<=epsilon or y :
    print("division by zero")
    exit()
else :
    print((((z - 23.1) * (2 ** x + 2.2)) / (y - 21.1)) - 3.2)

# функция abs() - модуль числа
# функция exit() - выход из программы


