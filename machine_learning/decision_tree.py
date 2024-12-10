"""
    A decision tree is a powerful tool in data mining and machine learning.
    - What it is:
    It is a flowchart-like structure. Nodes and branches are the main components.
    The nodes represent decision - making points or attributes,
    and the branches show the possible outcomes or values of those attributes.
    For example, if you are building a decision tree to predict whether a customer will buy a product,
    a node might be "Customer's Age", and the branches could be "Under 30", "30 - 50", and "Over 50".
    - How it works:
    It starts from a root node. The root node is the most important decision factor.
    As you move down the tree through different levels of nodes and branches, more specific decisions are made.
    The process continues until a leaf node is reached. Leaf nodes are the endpoints that represent
    the final classification or prediction result.
    For instance, in a tree for weather forecasting, the root node could be "Cloud Cover",
    and as you follow the branches based on different levels of cloud cover and other factors like
    humidity and wind speed, you eventually get to a leaf node that says "Sunny" or "Rainy".
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建模型: Decision Tree
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
print(f"y_test = {y_test} \n predictions = {y_pred}")
