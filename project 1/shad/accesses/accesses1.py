class SomeClass:
    def __init__(self):
        self.normal_attribute = 0
        self._protected_attribute = 0
        self.__private_attribute = 0

    def print_private(self):
        print(self.__private_attribute)

c = SomeClass()
print(dir(c))
print(c._SomeClass__private_attribute)
c.print_private()