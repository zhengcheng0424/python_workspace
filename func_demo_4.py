"""
    4 dict 字典
"""

if __name__ == '__main__':
    # 4.1 get 添加元素
    person = {'name': 'Zhang San', 'age': 20, 'title': 'The outlaw'}
    print(person.get('name'))
    print(person.get('waaaaagh'))
    print(person.get('height', 'Unknown'))
    # 4.2 keys(), values(), items() 分别返回字典的键 值 键值对
    print(len(person))
    print(person.keys())
    print(person.values())
    print(person.items())
    # 4.3 update() 相当于两个字典的键值对的merge
    print(person.update({'age': 21, 'trait': 'notorious'}))
    print(person)


