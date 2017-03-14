class X:
    def __init__(self):
        self.x = 5

    def method1(self, a, b):
        return self.x + a + b


class A(X):
    def __init__(self):
        super().__init__()
        self.y = 6

    def method2(self, a, b):
        return a * b

    def method3(self):
        return self.x * self.y


a = A()
print(a.method1(2,3),end="\n\n")
print(a.method2(8,9),end="\n\n")
print(a.method3())

