import matplotlib.pyplot as plt


def plot_data(x_values, y_values):
    plt.plot(x_values, y_values, label="x-y values")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Plot Title")
    plt.show()


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    y = [10, 112, 133, 14, 15, 16]
    plot_data(x, y)
