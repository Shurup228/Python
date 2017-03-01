

def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

print(fib(5))
x = [fib(elem) for elem in range(1, 10)] # Концепт именуемый "list comprehension"

# Цикл for используется для того что бы "перебрать" все элементы какой либо итерируемой последовательности,
# в нашем случае это список


print(x)



