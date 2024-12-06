"""
    2 Logistic regression:
    Logistic regression is used for classification problems.
    For example, it can be used to determine whether an email is spam or not.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载数据集
data = load_iris()
x = data.data
y = data.target

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建模型
model = LogisticRegression()

# 训练模型
model.fit(x_train, y_train)

# 预测
predictions = model.predict(x_test)

# 模型评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy = {accuracy * 100:.2f}%")
print(f"x = {x} \n y = {y}")
print(f"y_test = {y_test} \n predictions = {predictions}")