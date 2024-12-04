"""
    2 字符串处理函数
"""

if __name__ == '__main__':
    # 2.1 split() 分割字符串
    sentence = 'python is awsome!'
    print(sentence, type(sentence))
    words = sentence.split()
    print(words, type(words), type(words[0]))
    # 2.2 join 连接字符串
    other_words = ['java', 'is', 'awsome', 'too']
    print(' '.join(words))
    print(' '.join(other_words))
    # 2.3 strip 去除首尾空白符
    text = '          Go is also awsome!       '
    clean_text = text.strip()
    print(clean_text)
    # 2.4 replace 替换子串
    print(clean_text.replace("Go", "Scala"))
    print(clean_text)  # 注意原字符串不会改变
    # 2.5 lower and upper
    print(clean_text.lower())
    print(clean_text.upper())
    print(clean_text)  # 注意原字符串不会改变