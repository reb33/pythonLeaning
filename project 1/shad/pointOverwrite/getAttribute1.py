# getAttribute вызывается при обращении к любым атрибутам, которые есть и которых нет
class MyClass:
    def __init__(self,x):
        self.x = x

    def __getattribute__(self, item):
        print("getAttribute "+str(item))
        return super().__getattribute__(item)

    def my_func(self):
        print("Hi my func")

    @staticmethod
    def my_static_func():
        print("Hi my static func")

class MyClass2:
    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        # атрибуты этого класса получать через super() иначе будет рекурсия
        return super().__getattribute__("x")+1

m = MyClass(8)
m.my_func()
m.y = 5
m.my_static_func()

print(m.y)

print("\n____________2________________")
m2 = MyClass2(9)
print(m2.x)
print(m2.y)


