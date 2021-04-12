from PIL import Image
import os, glob, sys, numpy as np
from sklearn.model_selection import train_test_split

img_dir = './data'
categories = ['Cat', 'Dog']
np_classes = len(categories)

image_w = 256
image_h = 256

pixels = image_w * image_h * 3

X = []
y = []

for idx, cat in enumerate(categories):
    img_dir_detail = img_dir + "/" + cat
    files = glob.glob(img_dir_detail + "/*.jpg")

    for i, f in enumerate(files):
        try:
            img = Image.open(f)
            img = img.convert("RGB")
            img = img.resize((image_w, image_h))
            data = np.asarray(img)
            # Y는 0 아니면 1이니까 idx값으로 넣는다.
            X.append(data)
            y.append(idx)
            if i % 300 == 0:
                print(cat, " : ", f)
        except Exception as e:
            print(e)
            print(cat, str(i) + " 번째에서 에러 ")
X = np.array(X)
Y = np.array(y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

xy = (X_train, X_test, Y_train, Y_test)
print(xy)
np.save("./numpy_data/binary_image_data.npy", xy)
