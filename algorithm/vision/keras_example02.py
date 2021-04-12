import numpy as np
import tensorflow.keras as keras
import tensorflow.keras.datasets.mnist as mnist
from tensorflow.keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.dtype)
print(train_labels.shape)
print(train_labels[0])
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = keras.models.Sequential()
dense1 = keras.layers.Dense(32, activation='relu', input_shape=(784,))
dense2 = keras.layers.Dense(10, activation='softmax')

model.add(dense1)
model.add(dense2)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# model.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)