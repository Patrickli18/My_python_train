import os

# 关闭 TensorFlow 部分日志
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import sys
import graphviz
import numpy as np
import scipy
import sklearn
import pandas as pd
import keras
import tensorflow as tf

print("=" * 55)
print("Python 环境测试")
print("=" * 55)

print("Python:", sys.version.split()[0])
print("Graphviz:", graphviz.__version__)
print("NumPy:", np.__version__)
print("SciPy:", scipy.__version__)
print("Scikit-learn:", sklearn.__version__)
print("Pandas:", pd.__version__)
print("Keras:", keras.__version__)
print("TensorFlow:", tf.__version__)

print("\n" + "=" * 55)
print("功能测试")
print("=" * 55)

# 1. NumPy
a = np.array([1, 2, 3, 4, 5])
print("NumPy 求平均值:", np.mean(a))

# 2. SciPy
from scipy import stats
print("SciPy 标准差:", stats.tstd(a))

# 3. Pandas
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 95]
})
print("\nPandas DataFrame:")
print(df)

# 4. Scikit-learn
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

print("\nScikit-learn 预测 X=6:")
print(model.predict([[6]]))

# 5. Graphviz
dot = graphviz.Digraph()
dot.node("A", "Start")
dot.node("B", "End")
dot.edge("A", "B")

print("\nGraphviz DOT:")
print(dot.source)

# 6. TensorFlow
tensor = tf.constant([[1, 2], [3, 4]])
print("\nTensorFlow 张量:")
print(tensor)
print("TensorFlow 计算结果:")
print(tf.matmul(tensor, tensor))

# 7. Keras 神经网络
print("\nKeras 神经网络训练测试:")

model = keras.Sequential([
    keras.layers.Input(shape=(1,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

X_train = np.array([[1], [2], [3], [4]], dtype=np.float32)
y_train = np.array([[2], [4], [6], [8]], dtype=np.float32)

model.fit(X_train, y_train, epochs=5, verbose=0)

print("Keras 模型训练成功！")

print("\n" + "=" * 55)
print("所有库测试完成！")
print("=" * 55)