from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt
import pickle

X = []
Y = []
with open('dog.pickle', 'rb') as f:
    X, Y = pickle.load(f)
    print("dogX:", X.shape)
    print("dogY:", Y.shape)

with open('cat.pickle', 'rb') as f:
    tx, ty = pickle.load(f)
    print("catX:", X.shape)
    print("catY:", Y.shape)
    X = np.append(X, tx, axis=0)
    Y = np.append(Y, ty)

print(X.shape)
print(Y[0], Y[700])

# Generator 생성
datagen = ImageDataGenerator(shear_range=0.5,
                             zoom_range=[0.8, 2.0],
                             rotation_range=15,
                             width_shift_range=0.1,
                             height_shift_range=0.1,
                             horizontal_flip=True,
                             vertical_flip=False)

# prepare iterator
itr = datagen.flow(X, y=Y, batch_size=32)

X = []
Y = []

# make image
for i in range(2000):
    # generate batch of image
    batch = itr.next()
    Y = np.append(Y, batch[1])
    # convert to unsigned integers for viewing
    image = batch[0].astype('uint8')
    if i == 0:
        X = np.copy(image)
        print(image.shape)
        print(Y)
    else:
        X = np.append(X, image, axis=0)
    if i % 600 == 0:
        print("now=", i)
        print(X.shape)

X = np.array(X)
print('X.shape=', X.shape)
print(Y.dtype, Y.shape, Y, sep='\n')

data = (X, Y)

with open('dog-cat-data.pickle', 'wb') as f:
    pickle.dump(data, f)
