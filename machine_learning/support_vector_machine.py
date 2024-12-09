"""
A Support Vector Machine is a supervised machine - learning algorithm.
It's mainly used for classification tasks,
although it can also be applied to regression
The Concept of Separating Hyperplane
In a classification problem with two-dimensional data (for example, data points with two features),
SVM tries to find a line (in 2D, a hyperplane in higher dimensions)
that best separates the data points of different classes.
For instance, if you have a set of data points representing apples and oranges, based on features like size and color,
SVM will find a line that separates apples from oranges as clearly as possible.
The goal is to maximize the margin. The margin is the distance between
the hyperplane and the closest data points of each class.
These closest data points are called support vectors.
Kernel Trick
SVM can handle non-linearly separable data using the kernel trick. When the data can't be separated by
a simple straight line (in 2D) or hyperplane, a kernel function is used to transform the data into a higher-dimensional
space where it might be linearly separable. For example, consider data points that form a circle in a 2D
space. In the original 2D space, it's not possible to separate the inner and outer points with a straight line. But
by using a kernel function like the radial basis function (RBF), the data can be mapped to a higher - dimensional
space where a separating hyperplane can be found.
Applications
SVMs are widely used in many fields. In bioinformatics, they can be used to classify genes or proteins
into different categories. In text classification, SVMs can classify documents as spam or non-spam,
or into different topics. In image recognition, SVMs can help in classifying objects in images,
such as differentiating between different types of vehicles in traffic images.
Advantages
SVMs are effective in high-dimensional spaces. They work well even when the number of features is much
larger than the number of samples. They have good generalization ability. When properly tuned, they can provide
accurate predictions on new, unseen data. Disadvantages The computational cost of training an SVM can be high,
especially when dealing with a large number of data points and complex kernel functions. Selecting the appropriate
kernel and its parameters can be a challenging task and requires some prior knowledge or experimentation.

分离超平面的概念
在二维数据（例如，具有两个特征的数据点）的分类问题中，支持向量机试图找到一条能将不同类别数据点尽可能清晰分开的直线
（在二维中是直线，在更高维度中则是超平面）。
例如，如果你有一组代表苹果和橙子的数据点，依据诸如大小和颜色等特征，支持向量机将会找到一条能尽可能清楚地区分苹果和橙子的直线。
其目标是使间隔最大化。间隔就是超平面与每个类别中距离它最近的数据点之间的距离。这些距离超平面最近的数据点被称为支持向量。
核技巧
支持向量机能够利用核技巧来处理非线性可分的数据。当数据无法通过简单的直线（在二维情况下）或超平面进行分离时，
就会使用核函数将数据转换到一个更高维度的空间中，在那里数据或许就变成线性可分的了。例如，设想在二维空间中有一些数据点构成一个圆形。
在原始的二维空间中，不可能用一条直线将内部和外部的数据点分开。但通过使用像径向基函数（RBF）这样的核函数，数据可以被映射到一个更高维度的空间，
在那里就能找到一个分离超平面了。
应用领域
支持向量机在众多领域都有广泛应用。在生物信息学中，它们可用于将基因或蛋白质分类到不同类别中。
在文本分类方面，支持向量机能将文档分类为垃圾邮件或非垃圾邮件，或者划分到不同主题类别中。
在图像识别领域，支持向量机有助于对图像中的物体进行分类，比如区分交通图像中不同类型的车辆。
优势
支持向量机在高维空间中很有效。即便特征数量远多于样本数量时，它们也能很好地发挥作用。
它们具有良好的泛化能力。经过适当调整后，它们能够对新的、未见过的数据提供准确的预测。
劣势
训练支持向量机的计算成本可能很高，尤其是在处理大量数据点以及复杂核函数的时候。
选择合适的核函数及其参数可能是一项颇具挑战性的任务，需要具备一些先验知识或者通过反复试验来确定。

"""

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

data = load_iris()
x, y = data.data, data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建模型：SVC
model = SVC()

model.fit(x_train, y_train)
predictions = model.predict(x_test)

print(f"accuracy_score is {accuracy_score(y_test, predictions) * 100:.2f} %")
print(x_train, y_train)
print(y_test, predictions)
