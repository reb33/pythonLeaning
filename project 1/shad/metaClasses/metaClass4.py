class Meta(type):
    def __init__(cls, name, basses, attrs):
        super().__init__(name, basses, attrs)
        for name, attr in attrs.items():
            if callable(attr):
                short_name = attr.__name__[0].upper()
                setattr(cls, short_name, attr)


class A(metaclass=Meta):
    def foo1(self):
        print("Hi")

    def bar1(self):
        print("Bar")

x = A()
x.foo1()
x.bar1()
x.F()
x.B()
