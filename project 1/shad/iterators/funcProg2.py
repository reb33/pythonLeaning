import itertools
from generator2 import my_range_gen
from iterator1 import MyRange

for x in itertools.islice(my_range_gen(0,10,1), 1, 8, 2):
    print(x,end=" ")

print()
for x in itertools.islice(MyRange(10), 2, 9, 2):
    print(x, end=" ")

print()
for x in itertools.chain(my_range_gen(0, 5, 1), my_range_gen(10, 15, 1)):
    print(x, end=" ")