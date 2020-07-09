import tensorflow as tf

cifar10 = tf.keras.datasets.cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 可视化训练集输入特征的第一个元素
print(x_train[0].shape)  # 绘制图片

