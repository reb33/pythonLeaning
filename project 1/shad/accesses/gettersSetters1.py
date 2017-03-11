class SomeClass1:
    def __init__(self):
        self.__attr = 1000

    def __get_attr(self):
        print("getter attr")
        return self.__attr

    def __set_attr(self, val):
        print("setter attr")
        assert isinstance(val, int)
        self.__attr = val

    attr = property(__get_attr, __set_attr)

x = SomeClass1()
print(x.attr)
x.attr = 2000
print(x.attr)

class SomeClass2:
    def __init__(self):
        self.__volt = 1000

    @property
    def volt(self):
        '''Get current volt'''
        print ("getter volt")
        return self.__volt

    @volt.setter
    def volt(self, val):
        print("setter volt")
        assert isinstance(val, int)
        self.__volt = val

print()
c = SomeClass2()
# print(c.volt.__doc__)
print(c.volt)
c.volt = 2000
print(c.volt)
