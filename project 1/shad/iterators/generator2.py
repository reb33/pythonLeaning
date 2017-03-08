def my_range_gen(begin, end, step):
    current = begin
    while current<end:
        yield current
        current += step


def main():
    for x in my_range_gen(0, 5, 1):
        print(x,end=" ")

if __name__ == "__main__":
    main()
