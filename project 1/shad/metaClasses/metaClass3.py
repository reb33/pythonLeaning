class Meta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.f = lambda self: "qwerty"


class A(metaclass=Meta):
    pass

a = A()
print(a)
print(a.f())