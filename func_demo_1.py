"""
    1 基础函数
"""


if __name__ == '__main__':
    # 1.1 print
    print('Aloha python!')
    # 1.2 len 可以返回列表，字符串，字典等对象的长度
    my_list = [1, 2, 3, 6, 66, 666]
    print(len(my_list))
    my_str = 'waaaaaaaaaaaaagh'
    print(len(my_str))
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(len(my_dict))
    # 1.3 type 查看类型
    x = 10
    print(type(x))
    # 1.4 int(), float(), str() 类型转换
    x = int("10")
    y = float("3.141592653589793")
    z = str(3339)
    print(type(x), type(y), type(z))
    # 1.5 input 控制台交互，等待用户输入
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    print(f"Your name is {name} and you are {age} years old")
    # 1.6 range 生成数字序列(0到range-1)
    for i in range(4):
        print(f"iter->{i}")  # 输出：iter->0,1,2,3
    # 1.7 sum 求和
    numbers = list(range(10))
    print(numbers)
    total = sum(numbers)
    print(total)
    # 1.8 max, min
    print(max(numbers))
    print(min(numbers))
    # 1.9 sorted() 排序
    messy = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    neat = sorted(messy)
    print(messy, neat)
    # 1.10 help
    help(print)