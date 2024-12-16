"""
1. **原理概述**
   - XGBoost (eXtreme Gradient Boosting) 是一种基于梯度提升决策树(GBDT)的机器学习算法。
   它的基本原理是通过构建多个决策树，并将这些树的预测结果累加起来得到最终的预测。
   与传统的GBDT相比，XGBoost在目标函数的定义和优化、树的构建方式等方面有诸多改进。
   - 在训练过程中，它以最小化损失函数为目标。
   每次迭代都会添加一个新的决策树来拟合上一次预测结果的残差（在回归问题中）或梯度（在分类问题中利用对数似然损失函数的梯度）。
   例如，在预测房屋价格的回归任务中，第一个决策树可能会对价格做出一个初步的估计，
   然后后续的决策树会尝试去纠正第一个决策树的错误，也就是拟合残差，使得最终的预测结果越来越准确。
2. **模型结构特点**
   - **正则化**：XGBoost在目标函数中加入了正则项，用于控制模型的复杂度。这有助于防止过拟合，使得模型在训练数据和测试数据上都能有较好的性能。
   正则项包括对叶子节点数量和叶子节点权重的惩罚。
   比如，当构建的决策树过于复杂，叶子节点过多时，正则项会使模型的损失函数增大，从而在训练过程中避免这种过于复杂的情况。
   - **列抽样**：它支持列抽样（column subsampling），类似于随机森林中的特征抽样。在每次迭代构建树时，可以随机选择一部分特征来进行树的构建。
   这不仅可以降低计算成本，还能在一定程度上防止过拟合，并且有助于发现更鲁棒的特征组合。
   - **树的生长策略**：XGBoost采用了深度优先（depth - first）的树生长策略，并且可以通过设置参数来控制树的最大深度等生长方式。
   这种策略可以快速找到有区分性的特征组合，同时也便于并行计算。
3. **应用场景**
   - **数据竞赛**：在许多数据科学竞赛（如Kaggle竞赛）中，XGBoost是非常受欢迎的算法。
   无论是预测客户是否会购买产品（分类问题）还是预测产品的销量（回归问题），它都能发挥很好的作用。
   例如，在预测泰坦尼克号乘客是否存活的竞赛问题中，XGBoost可以利用乘客的年龄、性别、船票等级等特征进行高效的分类。
   - **工业界应用**：在金融领域，用于信用风险评估、股票价格预测；在电商领域，用于商品销量预测、用户购买行为预测等。
   以信用风险评估为例，银行可以利用客户的收入、信用记录、贷款历史等众多信息，通过XGBoost模型来判断客户是否会违约。
4. **优点**
   - **高效性**：XGBoost在处理大规模数据集时表现出色，其内部的优化算法使得模型训练和预测速度都比较快。
   它采用了近似直方图算法来计算特征的分布，减少了计算量。
   例如，在处理包含数百万条记录的数据集时，相比一些传统的机器学习算法，它能够更快地完成训练并给出准确的预测。
   - **准确性高**：由于其强大的模型结构和优化算法，它通常能够获得比其他同类算法更高的准确性。
   通过合理的参数设置和特征工程，它可以挖掘出数据中复杂的模式。
   - **鲁棒性好**：对缺失数据有较好的处理能力，并且能够在不同类型的数据（数值型、类别型等）上正常工作。
   对于数据中的噪声也有一定的抵抗力，通过正则化等手段可以减少噪声的影响。
5. **缺点**
   - **参数较多**：XGBoost有大量的参数需要调整，对于初学者来说，理解和选择合适的参数是一个挑战。
   例如，学习率、树的数量、树的最大深度等参数都会影响模型的性能，不恰当的参数设置可能导致过拟合或欠拟合。
   - **解释性相对较弱**：虽然决策树本身有一定的可解释性，
   但XGBoost是由多个决策树组成的集成模型，其解释性比单个简单的模型（如线性回归）要差。
   很难直观地解释模型为什么做出某个特定的预测。
"""

import xgboost as xgb
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
model = xgb.XGBClassifier()

# 训练模型
model.fit(x_train, y_train)

# 预测
predictions = model.predict(x_test)

# 模型评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")