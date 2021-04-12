import numpy as np
import pickle

a = ()
b = ()

with open('./data/category.pickle', 'rb') as f:
    a, b = pickle.load(f)

print(a.shape, b.shape)

for i in range(30):
    print(b[ i * 100])
