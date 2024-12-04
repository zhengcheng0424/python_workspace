"""
    3 list处理函数
"""

if __name__ == '__main__':
    # 3.1 append 添加元素
    fruits = ['apple', 'banana', 'orange']
    print(fruits.append('grapes'))  # None 无返回值
    print(fruits)
    # 3.2 extend 将另外一个列表所有元素添加到当前列表
    print(fruits.extend(['pineapple', 'pineapple', '', 'apple']))  # None 无返回值
    print(fruits)  # 重复的元素照加不误
    # 3.3 insert 在指定位置插入元素
    print(fruits.insert(1, fruits[1]))
    print(fruits)  # 重复的元素照加不误
    # 3.4 remove 删除元素
    print(fruits.remove('pineapple'))
    print(fruits)  # 重复的元素只删一次
    print(fruits.remove('pineapple'))
    print(fruits)  # 删两次删干净了
    # 3.5 pop 删除并返回列表中的最后一个元素
    print(fruits.pop())
    print(fruits)
    print(fruits.pop())
    print(fruits)