"""
K - 近邻算法（K-Nearest Neighbors，KNN）是一种简单且直观的监督式机器学习算法。
它主要用于分类问题，不过也能应用于回归问题。其核心思想是基于样本之间的距离来判断未知样本的类别或预测数值。

1. 工作原理
1.1 分类情况：
假设有一个包含多种类别样本的训练数据集。当需要对一个新的测试样本进行分类时，KNN 会计算这个测试样本与训练集中所有样本的距离。
距离的度量方式有多种，如欧几里得距离（在二维空间中，对于两点和，欧几里得距离）、曼哈顿距离（在二维空间中，对于两点和，曼哈顿距离）等。
然后，按照距离从小到大的顺序选择 K 个最邻近的训练样本。
例如，在一个区分动物是猫还是狗的问题中，假设 K = 5，找到距离新样本最近的 5 个邻居。
最后，统计这 K 个近邻所属的类别，新样本就被分类为这 K 个近邻中出现次数最多的类别。
比如在上述例子中，如果 5 个近邻中有 3 个是狗，2 个是猫，那么新样本就被分类为狗。
1.2 回归情况：
同样先计算测试样本与训练集中所有样本的距离，选择 K 个最近邻。
然后，不是统计类别，而是对这 K 个近邻对应的目标数值（例如房屋价格）求平均值，
这个平均值就作为对测试样本的预测数值。
例如，要预测一套房子的价格，找到离它最近的 K 套房子的价格，计算这些价格的平均值作为预测价格。
2. 重要参数 —— K
K 值的选择对 KNN 算法的性能有很大影响。如果 K 值较小，模型容易受到噪声的影响，产生过拟合。
例如，K = 1 时，新样本的类别直接由最近的一个邻居决定，很可能因为这个邻居是一个异常值而导致分类错误。
相反，如果 K 值较大，模型会更平滑，但可能会忽略掉数据中的局部特征，导致欠拟合。
例如，在一个数据分布不均匀的情况下，K 值过大可能会把新样本分类到占比大但实际距离较远的类别中。
3. 优点
简单易懂，容易实现。不需要复杂的训练过程，是一种基于实例的学习算法，直接使用训练数据进行预测。
能够处理多分类问题，而且对数据的分布没有特别的要求，理论上可以处理任何分布的数据。
4. 缺点
计算成本高。每次对新样本进行预测时，都需要计算它与所有训练样本的距离，当训练数据集很大时，计算时间会很长。
对数据的维度灾难比较敏感。随着数据维度的增加，样本之间的距离计算变得复杂，而且样本在高维空间中变得更加稀疏，导致很难找到真正有意义的近邻。
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# 加载数据集
data = load_iris()
X = data.data
y = data.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型: KNN K的值的选择非常重要
k_value = 3
model = KNeighborsClassifier(n_neighbors=k_value)

# 训练模型
model.fit(X_train, y_train)

# 预测
predictions = model.predict(X_test)

# 模型评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")
