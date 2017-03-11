class MyClass1:
    def __init__(self, x):
        self.x = x

    def __setattr__(self, key, value):
        print("setattr ({}, {})".format(key, value))
        # установка атрибута выполнять через super() иначе будет рекурсия
        super().__setattr__("x",value)

myclass = MyClass1(5)
print(myclass.x)
myclass.y = 8
print(myclass.x,end="\n\n")


print(myclass.y)