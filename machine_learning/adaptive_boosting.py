"""
AdaBoost (Adaptive Boosting) 是一种重要的集成学习算法，以下是简单介绍：

**一、基本原理**

1. **概念**
   - AdaBoost的核心思想是将多个弱分类器组合成一个强分类器。
   弱分类器是指那些分类准确率只比随机猜测稍好一点的分类器。
   例如，一个简单的决策树桩（只有一层的决策树），它可能在某些数据上能做出比随机分类更好的判断，但单独使用时效果有限。
   - 通过对训练数据进行多次抽样和训练不同的弱分类器，并且根据每个弱分类器的表现来调整训练数据的权重，使得后续的弱分类器更加关注之前被错误分类的样本。
2. **工作流程**
   - 首先，初始化训练数据的权重，每个样本的权重相同。然后，使用带有权重的训练数据训练第一个弱分类器。
   - 计算第一个弱分类器在训练数据集上的错误率。根据错误率，计算这个弱分类器的权重，错误率越低，权重越高。
   - 根据弱分类器的权重更新训练数据的权重。被错误分类的样本的权重会增加，这样下一个弱分类器就会更加关注这些难分类的样本。
   - 重复上述过程，训练多个弱分类器。最后，将这些弱分类器组合起来，通过加权投票的方式得到最终的强分类器。
   比如，对于一个二分类问题，假设我们有三个弱分类器，它们的权重分别为0.1、0.3和0.6
   ，当对一个新样本进行分类时，每个弱分类器会给出一个分类结果（+1或 - 1），将这些分类结果乘以相应的权重并求和，根据最终的和的正负来确定样本的类别。

**二、应用场景**

1. **分类问题**
   - AdaBoost在二分类和多分类问题中都有广泛应用。例如在垃圾邮件分类中，文本数据被转换为特征向量后，
   可以使用AdaBoost将多个简单的文本分类器（如基于词袋模型的分类器）组合起来，有效提高分类的准确率。
   - 在医疗诊断领域，对于疾病的分类（如区分良性和恶性肿瘤），AdaBoost可以整合多种医疗检测指标（如血液检测指标、影像特征等）构建的弱分类器，增强分类的可靠性。
2. **回归问题（AdaBoost.R2）**
   - 除了分类，AdaBoost的变体也可以用于回归问题。它可以将多个弱回归器组合起来预测连续型的数值，比如预测股票价格、房屋价格等。
   不过在回归应用中，计算弱回归器权重和更新样本权重的方式与分类情况有所不同。

**三、优点和缺点**

1. **优点**
   - 能够有效提高分类的准确性。通过组合多个弱分类器，可以克服单个弱分类器的局限性。
   - 不容易过拟合。因为它是通过不断调整数据权重，关注难分类的样本，而不是简单地记忆训练数据的模式。
   - 可以使用各种类型的弱分类器，如决策树、神经网络等，具有很强的灵活性。
2. **缺点**
   - 对异常值比较敏感。由于它会不断提高被错误分类样本的权重，如果数据中有异常值，可能会导致模型过度关注这些异常值，从而影响模型的性能。
   - 训练时间可能较长。因为需要训练多个弱分类器，并且在每次训练后要更新样本权重等操作，所以在数据量较大或者弱分类器比较复杂时，训练成本较高。
"""

from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# 加载数据集
data = load_iris()
x = data.data
y = data.target

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建模型: AdaBoost(Adaptive Boosting)
model = AdaBoostClassifier()

# 训练模型
model.fit(x_train, y_train)

# 预测
predictions = model.predict(x_test)

# 模型评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")
