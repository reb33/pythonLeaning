from multiprocessing import Pool


def calc(val):
    return val ** 2


def main():
    p = Pool(processes=4)
    ret = p.map(calc, range(10))
    print(ret)


if __name__ == "__main__":
    main()