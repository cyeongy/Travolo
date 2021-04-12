from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import pickle

base_path = "./category"

category = []
res_path = []

# 분석용 이미지 경로 파싱, 저장
for gdx, grand in enumerate(os.listdir(base_path)):
    mothers = os.path.join(base_path, grand)
    for mdx, mother in enumerate(os.listdir(mothers)):
        sons = os.path.join(mothers, mother)
        for sdx, son in enumerate(os.listdir(sons)):
            category.append(1000 * (gdx + 1) + 100 * (mdx + 1) + (sdx + 1))
            res_path.append(os.path.join(sons, son))

# 이미지, 라벨 리스트
X = []
Y = []

# 경로에 있는 이미지 리사이즈 후 행렬로 변환 후 라벨과 함께 저장
for idx, path in enumerate(res_path):
    img_path = os.listdir(path)
    for my_path in img_path:
        if path.find('webp') != -1:
            continue
        final_path = os.path.join(path, my_path)
        # print(img_path)
        # img = load_img(final_path)
        # img = img.resize((80, 80))
        # X.append(img_to_array(img))
        Y.append(category[idx])


# 용량을 줄이기 위해 float32에서 uint8로 저장
X = np.array(X, dtype='uint8')
print(len(Y))

tple = (X, Y)

# 분석용 파일 저장

# with open('./data/category_small.pickle', 'wb') as f:
#     pickle.dump(tple, f)