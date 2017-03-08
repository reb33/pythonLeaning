from itertools import product, zip_longest, tee
from iterator1 import MyRange
from generator2 import my_range_gen


def smth_loop(width, height, depth):
    shape = [width, height, depth]
    for i, j, z in product(*map(range, shape)):
        print("("+str(i), str(j), str(z)+")",end=" ")


def grouper(iterable, n, fillValue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillValue)


def main():
    smth_loop(2, 5, 7)
    print()
    for x in grouper(MyRange(10), 3, "z"):
        print(x)
    for x in tee(my_range_gen(1, 10, 1), 2):
        print(list(x))


if __name__ == "__main__":
    main()