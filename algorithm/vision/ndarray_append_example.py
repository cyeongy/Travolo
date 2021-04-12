import numpy as np
import json, pickle


arr = np.array(
    [[
        [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [2, 3, 4],
            [2, 3, 4]
        ],
        [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [2, 3, 4],
            [2, 3, 4]
        ],
        [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [2, 3, 4],
            [2, 3, 4]
        ],
        [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [2, 3, 4],
            [2, 3, 4]
        ],
        [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [2, 3, 4],
            [2, 3, 4]
        ]
    ]
    ]
)

arr1 = np.array([5])

# print(arr)
print(arr.shape)
print(arr1.shape)

a = (arr, arr1)

print(a)

with open('test.pickle', 'wb') as f:
    pickle.dump(a, f)