class A:
    pass


def retA(classname, bases, attrs):
    return A


class C(metaclass=retA):
    def f(self):
        return "abc"


c = C()
print(c)
print(c.f())
