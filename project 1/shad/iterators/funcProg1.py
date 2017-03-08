import itertools
import functools

print(list(filter(lambda x: x % 2 == 0, range(10))))
print(list(x for x in range(10) if x % 2 == 0))

print(list(map(lambda x: x**2, range(10))))
print(list(x**2 for x in range(10)))

print()
d = enumerate(range(5,10))
print(list(d))
print(list(d))

print(functools.reduce(lambda x,y:x*y, range(1,6)))

for x in itertools.product(range(5), range(5, 10)):
    print(x,end=" ")

print()
for x in itertools.combinations(range(5), 3):
    print(x,end=" ")

print()
for x in itertools.permutations(range(5), 3):
    print(x,end=" ")

print()
for x in itertools.combinations_with_replacement(range(5), 3):
    print(x,end=" ")
