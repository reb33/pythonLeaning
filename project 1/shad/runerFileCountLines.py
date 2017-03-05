import sys
import argparse


def count_line(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            count+=1
        return count


def count_symbols(filename, index_line):
    with open(filename) as f:
        current = 0
        for line in f:
            current += 1
            if current == index_line:
                return len(line)

#   Через sys.argv
# def main():
#     if len(sys.argv) == 1:
#         print("Too few arguments")
#     else:
#         print(count_line(sys.argv[1]))


def main():
    parser = argparse.ArgumentParser()
    parser.description = '''With 1 argument return count rows in file.\n
    With 2 arguments return count symbols in line of file'''
    parser.add_argument(
        "filename",
        help="file for scanning"
    )
    parser.add_argument(
        "--line","-l",
        help="line for scanning",
        type=int,
        default=None
        # ,required=True
    )
    args = parser.parse_args()
    if args.line is None:
        print(count_line(args.filename))
    else:
        print(count_symbols(args.filename, args.line))

if __name__ == "__main__":
    main()
