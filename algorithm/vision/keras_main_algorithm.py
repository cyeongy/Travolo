import pickle
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import tensorflow as tf
from tensorflow.keras.utils import to_categorical

with open('./data/category_small.pickle', 'rb') as f:
    X, Y = pickle.load(f)
t = []

for i in Y:
    t.append(i // 100)
Y = t

train_images, test_images, train_labels, test_labels = train_test_split(X, Y,
                                                                        test_size=0.2,
                                                                        random_state=6974)

output_number = len(set(train_labels))

train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 모델 만들기
model = keras.models.Sequential()

model.add(keras.layers.Conv2D(32, (3, 3), padding='same', input_shape=train_images[0].shape, activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(1024, activation='relu'))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Dense(len(train_labels[0]), activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=12, batch_size=128)
test_loss, test_acc = model.evaluate(test_images, test_labels)

model.save('/content/drive/MyDrive/Colab Notebooks/classify.h5')
