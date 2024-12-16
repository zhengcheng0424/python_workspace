"""
CatBoost是另一个高效的梯度提升框架，特别适合处理分类特征。
比如，预测用户行为。

1. **基本原理**
   - CatBoost（Categorical Boosting）是一种梯度提升算法，主要用于处理分类和回归问题。
   它在梯度提升框架的基础上，对于类别型变量有出色的处理能力。其核心原理是通过构建多棵决策树来逐步减少预测误差。
   与其他梯度提升算法类似，CatBoost也是基于前一棵树的残差来构建下一棵树。
   - 例如，在预测房屋价格（回归问题）时，第一棵决策树可能做出一个初步的价格估计，后续的树会根据前一棵树预测价格与实际价格的差异（残差）来进行更精准的估计。

2. **对类别型变量的处理**
   - **有序目标统计量（Ordered Target Statistics）**：CatBoost在处理类别型变量时，采用了一种独特的方法。它计算有序目标统计量来编码类别型变量。
   对于每个类别型变量，它会根据训练数据中该类别对应的目标变量的均值等统计信息来进行编码。
   - 比如，在一个预测用户购买产品与否（目标变量）的问题中，有一个类别型变量是用户所在城市。
   CatBoost会计算每个城市中购买产品的用户比例等统计信息，并将这些信息作为该城市这个类别型变量的编码，
   从而有效地将类别型变量转化为数值型变量用于模型构建。

3. **模型特点**
   - **防止过拟合**：CatBoost内置了一些防止过拟合的机制。它采用了一种叫做“叶节点值平滑”的技术，通过在树的叶节点之间共享信息来减少模型的方差。
   同时，它还可以通过调整树的深度、学习率等参数来控制模型的复杂度，提高模型的泛化能力。
   - **支持GPU加速**：可以利用GPU（图形处理器）进行计算加速。在处理大规模数据集或者复杂模型时，GPU加速能够显著提高模型的训练速度。
   例如，在处理海量的电商交易数据或者高维的图像数据等场景下，GPU加速能够让CatBoost更快地完成训练。

4. **应用场景**
   - **分类问题**：广泛应用于文本分类、图像分类等领域。在文本分类中，如对新闻文章进行分类（体育、娱乐、财经等类别），
   CatBoost可以有效地利用文章中的词汇、语法等特征，结合对类别型变量（如文章来源等）的处理，提高分类的准确性。
   - **回归问题**：在预测产品销量、股票价格等问题上表现出色。以产品销量预测为例，
   它可以利用产品的属性、市场环境等多种因素，包括类别型因素（如产品品牌等）来进行精准的销量预测。

5. **优点**
   - **对类别型数据友好**：不需要复杂的类别型变量预处理，就能很好地将类别型变量融入模型构建，这节省了大量的数据预处理时间和精力。
   - **性能优异**：在许多实际应用中，CatBoost能够提供高精度的预测结果，并且通过防止过拟合机制，在不同数据集上有较好的稳定性。
   - **高效训练**：支持GPU加速使得它在处理大数据和复杂模型时能够快速训练，提高了模型开发的效率。

6. **缺点**
   - **计算资源需求高**：尤其是在使用GPU加速时，需要有合适的GPU设备支持。对于一些没有GPU资源或者计算资源有限的环境，可能无法充分发挥其优势。
   - **参数调整复杂**：和其他高级机器学习算法一样，CatBoost有许多参数需要调整，对于初学者来说，找到合适的参数组合以达到最佳性能可能是一个挑战。

"""

import catboost as cb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# 加载数据集
data = load_iris()
x = data.data
y = data.target

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建模型
model = cb.CatBoostClassifier()

# 训练模型
model.fit(x_train, y_train)

# 预测
predictions = model.predict(x_test)

# 模型评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")