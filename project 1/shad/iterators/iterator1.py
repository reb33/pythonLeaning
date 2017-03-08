class MyIterator:
    def __init__(self, end):
        self.end = end
        self.current = 0

    def __next__(self):
        if self.current == self.end:
            raise StopIteration()
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return MyIterator(self.end)


def main():
    print(list(MyRange(5)))

if __name__ == "__main__":
    main()
