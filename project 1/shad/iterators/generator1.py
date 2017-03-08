def gen1():
    yield 1
    yield "abc"
    yield [1, 2, 3]

for index, x in enumerate(gen1()):
    # print(x)
    print(str(index)+" - "+str(x))

print(gen1())
print((x, y) for x in range(5) for y in range(5, 10))
print(list((x, y) for x in range(5) for y in range(5, 10)))
