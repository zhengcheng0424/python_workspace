"""
    1 Linear Regression: a method for predicting the continuous values of an input
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

x = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([2, 4, 5, 6, 9, 11])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建模型
model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

# 可视化结果
plt.scatter(x, y, color='red', label='actual')
plt.plot(x, model.predict(x), color='blue', label='prediction')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.show()
