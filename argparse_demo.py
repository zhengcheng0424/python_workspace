import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    args = parser.parse_args()
    print(args.integers)
    return sum(args.integers)


# 用法：
# 在本目录命令行中输入：
# python argparse_demo.py 1 2 3 5
# 或者
# python argparse_demo.py -h·
if __name__ == '__main__':
    main()
