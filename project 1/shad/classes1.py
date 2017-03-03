class MyClass:
    def __init__(self, number, function):
        self.number = number
        self.function = function

    # def __init__(self):
    #     pass

    def set_number(self, number):
        self.number = number

    def set_function(self, function):
        self.function = function

    def count_and_run(self):
        for x in range(self.number):
            self.function(x)

x = []
myClass = MyClass(5, x.append)

# myClass.set_function(x.append)
# myClass.set_number(5)
myClass.count_and_run()
print(x)
print (x.append)
print(x.append(1))
