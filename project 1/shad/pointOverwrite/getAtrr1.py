class MyClass:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        print("getattr "+str(name))
        return self.x+1

myclass = MyClass(5)
print(myclass.y)
print(myclass.x)
print(myclass.y)
print(myclass.d)