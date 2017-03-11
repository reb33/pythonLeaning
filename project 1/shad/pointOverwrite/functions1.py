class SomeClass:
    pass

c = SomeClass()

setattr(c, "x", 5)
# equivalent c.x = 5

print (hasattr(c, "x"))
# проверяет выбрасывается ли исключение

print(getattr(c, "x"))
# equivalent c.someattr