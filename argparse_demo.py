import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    args = parser.parse_args()
    print(args.integers)
    return sum(args.integers)


if __name__ == '__main__':
    main()
