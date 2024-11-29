import pandas as pd


def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    return df


if __name__ == '__main__':
    example_2 = load_csv_data('example_2.csv')
    print(example_2.head)
    print(example_2)
