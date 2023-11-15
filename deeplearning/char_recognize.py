
# recognize mnist using tensorflow and keras
# https://www.tensorflow.org/tutorials/keras/classification
# https://www.tensorflow.org/tutorials/images/cnn
# author:   Wang Yong
# email:    dr.wangyong at hotmail.com
# version:  0.1
# date:     2023/11/12
# Pair programming with github copilot

import tensorflow as tf
from tensorflow import keras

# Load the dataset
# x_train: images, y_train: labels
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data("mnist.npz")

# Preprocess the data
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Define the model architecture
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
