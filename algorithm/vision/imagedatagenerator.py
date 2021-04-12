from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
np.random.seed(5)

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.5,
                                   zoom_range=[0.8, 2.0],
                                   rotation_range=15,
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   horizontal_flip=True,
                                   vertical_flip=False)
base_path = "./data/dog/"
dog_path = os.listdir("./data/dog")
print(dog_path[:2])
img_path = os.path.join(base_path, dog_path[0])
print(img_path)

img = load_img(img_path)
pimg = Image.open(img_path)
pimg = pimg.resize((800, 800))


pimg_tensor = img_to_array(pimg)
img_tensor = img_to_array(img)
# print(pimg_tensor)

pimg_tensor
t = img_tensor.reshape((1,)+img_tensor.shape)
print(type(pimg_tensor))
# plt.imshow(pimg_tensor/255)
# plt.show()
np.save(file='./data/sample/dog-800', arr=pimg_tensor)
# pimg.save('./data/sample/dog-800.jpg')

svd = np.load('./data/sample/dog-800.npy')
print(np.equal(svd, pimg_tensor))
