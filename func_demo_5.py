"""
    5 Python functions
"""
from functools import reduce

if __name__ == '__main__':
    # 5.1 map() batch operate 可以对列表中的每一个元素应用一个func
    messy = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    squared = list(map(lambda x: x ** 2, messy))
    print(squared)
    # 5.2 filter() 筛选出满足条件的元素
    evens = list(filter(lambda x: x % 2 == 0, messy))
    print(evens)
    # 5.3 reduce() 规约操作
    numbers = [1, 2, 3, 4, 5, 6]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)
    # 5.4 zip() 并行迭代
    names = ['Alice', 'Bob', 'Charlie']  # 当其中一个list不够长的时候先结束
    for name, number in zip(names, numbers):
        print(f'{name}: {number}')
    # 5.5 enumerate() 带索引的迭代
    friends = ['Alice', 'Bob', 'Charlie']  # 注意下面的index从0开始
    for index, friend in enumerate(friends):
        print(f'{index}: {friend}')
