import pickle
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
from tensorflow.keras.utils import to_categorical

with open('dog-cat-data.pickle', 'rb') as f:
    X, Y = pickle.load(f)

train_images, test_images, train_labels_origin, test_labels_origin = train_test_split(X, Y, test_size=0.2, random_state=6974)

train_labels = []
test_labels = []

for i in train_labels_origin:
    train_labels.append(0 if i == 'cat' else 1)

for i in test_labels_origin:
    test_labels.append(0 if i == 'cat' else 1)

print(train_images[0].shape)

train_images = train_images.astype('float32') / 255

test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = keras.models.Sequential()

model.add(keras.layers.Conv2D(32, (3, 3), padding='same', input_shape=train_images[0].shape, activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Dense(2, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)
