def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    text = read_file('test_example_1.txt')
    print(text)
    write_file('test_example_output_1.txt', text + '\n' + "New content here!")
