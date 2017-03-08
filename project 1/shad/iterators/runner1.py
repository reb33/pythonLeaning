import iterator1
import generator2

x = iterator1.MyRange(5)
print(list(x))
print(list(x),end="\n\n")

y = generator2.my_range_gen(0, 5, 1)
print(list(y))
print(list(y))
print(list(generator2.my_range_gen(0, 5, 1)))

