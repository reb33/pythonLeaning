import sys

class M(type):
    def f(cls):
        return "abs"


class C(metaclass=M):
    pass

a = C()

try:
    print(a.f())
except AttributeError as err:
    print(err)

print(C.f())