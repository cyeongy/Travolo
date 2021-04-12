from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

base_path = "./data/cat/"
dog_path = os.listdir("./data/cat")
print(len(dog_path))

X = []

for path in dog_path:
    if path.find('webp') != -1:
        continue
    print(path)
    print("sex")
