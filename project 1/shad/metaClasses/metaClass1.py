C = type("MyClass",
         object,
         {"f": lambda self: "abc"})

c = C()
print(c)
print(c.f())
