from sklearn.model_selection import train_test_split
import numpy as np
import pickle

with open('dog-cat-data.pickle', 'rb') as f:
    X, Y = pickle.load(f)

print(X.shape, Y.shape)

res = train_test_split(X, Y, test_size=0.2, random_state=6974)

a, b, c, d = res

for i in res:
    print(i.shape)


