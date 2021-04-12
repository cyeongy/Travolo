from tensorflow.python.client import device_lib
import os
from tensorflow.keras.models import load_model
import tensorflow as tf
import tensorflow.keras as keras
import PIL as pillow
import pickle


X = []
Y = []
with open('./data/category_small.pickle', 'rb') as f:
    X, Y = pickle.load(f)
t = []
for i in Y:
    t.append(i/100)
Y = t

# print(device_lib.list_local_devices())
print(tf.__version__, keras.__version__, pillow.__version__)
model = load_model('./classify_picture.h5')
res = model.predict(X[0])