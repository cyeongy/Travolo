from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fpath = './data/sample/dog-800.npy'
img_tensor = np.load(fpath)
test00 = np.expand_dims(img_tensor, 0)
test01 = np.append(test00, test00 / 2, axis=0)
print('img_tensor=', img_tensor.shape)
gen_test = np.copy(test00)

# Generator 생성
datagen = ImageDataGenerator(shear_range=0.5,
                             zoom_range=[0.8, 2.0],
                             rotation_range=15,
                             width_shift_range=0.1,
                             height_shift_range=0.1,
                             horizontal_flip=True,
                             vertical_flip=False)

# prepare iterator
itr = datagen.flow(test01, y=['dog', 'dog'], batch_size=1)  # , save_to_dir='./data/sample', save_prefix='gen_dog')

# figure 생성
fig = plt.figure(figsize=(30, 30))
Y = []
# make 9 image
for i in range(16):
    plt.subplot(4, 4, i + 1)

    # generate batch of image
    batch = itr.next()
    Y = np.append(Y, batch[1])
    print(Y)
    # convert to unsigned integers for viewing
    image = batch[0].astype('uint8')
    print('image=', image.shape)
    gen_test = np.append(gen_test, image, axis=0)

    if i == 0:
        print(image)
    # plot raw pixel data
    plt.imshow(image[0])

# show the figure
plt.title("Horizontal and Vertical Shift Augmentation")
plt.show()

print('gen_test=', gen_test.shape)
print(Y.dtype, Y.shape, Y, sep='\n')