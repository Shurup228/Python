
def absolute(a):
    if a < 0:
        return -a
    else:
        return a

first, sec = 1, 2


class MyFunc:
    def __init__(self, x, z, eps=10**-4):
        self.eps = eps
        self.x = x
        self.z = z

    def some_func(self):
        if (self.z - self.x**9 / 3) <= self.eps or \
                        absolute(self.z**2) <= self.eps:
            return print("error")
        else:
            return self.z + (self.x / (self.z**2 - absolute(self.x**2 / (self.z - self.x**9 / 3))))

    def some_func_builtin(self):
        if (
            (self.z - self.x ** 9 / 3) <= self.eps or
            abs(self.z ** 2) <= self.eps
        ):
            return print("error")
        else:
            return self.z + (self.x / (self.z**2 - abs(self.x**2 / (self.z - self.x**9 / 3))))

print(MyFunc(first, sec).some_func())
print(MyFunc(first, sec).some_func_builtin())
