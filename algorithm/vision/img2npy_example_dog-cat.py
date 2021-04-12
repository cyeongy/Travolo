    from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

base_path = "./data/dog/"
mpath = os.listdir("./data/dog")
print(len(mpath))

X = []

for path in mpath:
    if path.find('webp') != -1:
        continue
    img_path = os.path.join(base_path, path)
    # print(img_path)
    img = load_img(img_path)
    img = img.resize((80, 80))
    X.append(img_to_array(img))

X = np.array(X, dtype='uint8')
print(X.shape)
Y = np.array(['dog' for i in range(len(X))])
print(Y.shape)

tple = (X, Y)
print(tple)

# plt.figure(figsize=(3, 3))
# plt.imshow(X[0])
# plt.show()

with open('dog.pickle', 'wb') as f:
    pickle.dump(tple, f)