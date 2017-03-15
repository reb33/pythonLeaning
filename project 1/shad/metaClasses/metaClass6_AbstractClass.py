from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    @abstractmethod
    def f(self):
        print ("abc")


class B(A):
    def f(self):
        super().f()
        print("fgh")


class C(A):
    pass

x = B()
x.f()
try:
    y = C()
except TypeError as err:
    print(err.__class__.__name__+". "+ str(err))