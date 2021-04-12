# -*- coding: utf-8 -*-


from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from keras_preprocessing.image import load_img
import numpy as np
import os


# 학습에 사용된 카테고리 라벨
category = {1: "레포츠", 2: "인문", 3: "자연",
            11: "수상레포츠", 12: "육상레포츠", 13: "항공레포츠",
            21: "문화시설", 22: "역사관광지", 23: "휴양관광지",
            31: "자연관광지"}

# 분석서버의 학습모델, 이미지 저장 경로
model_path = '/home/analy/classify.h5'
base_path = '/home/analy/myproject/img'


# 이미지를 행렬로 변환
def img2npy(loaded_img):
    temp_img = loaded_img.resize((80, 80))
    arr = img_to_array(temp_img) / 255
    return np.expand_dims(arr, axis=0)


# 경로에 있는 이미지를 행렬로 변환
def load_img2npy(path):
    if os.path.split(path)[0] != '':
        return img2npy(load_img(path))
    temp_path = os.path.join(base_path, path)
    return img2npy(load_img(temp_path))


# 경로에 존재하는 학습모델 불러오기
# 기본 경로는 model_path와 동일
def load_kr_model(path='/home/analy/classify.h5'):
    return load_model(path)

'''
    학습 모델을 사용한 예측
    opt가 True이면 category의 key를 반환 False이면 value를 반환
    기본적으로 path 경로를 받고 설정에 따라 img 직접 입력 가능
'''
def predict(*args, **kwargs):
    if args is None:
        print("인자가 없습니다.")
        return

    if "img" in kwargs:
        my_img = img2npy(kwargs["img"])
    if "opt" in kwargs:
        if kwargs["opt"] is True:
            opt = True
    else:
        opt = False
    if "path" in kwargs:
        my_img = load_img2npy(kwargs["path"])
    else:
        my_img = load_img2npy(args[0])

    # 모델 불러오기 및 카테고리 예측
    my_model = load_kr_model()
    pr = my_model.predict_classes(my_img)
    if opt:
        return pr[0]
    return category[pr[0]]


if __name__ == '__main__':
    model = load_kr_model()
    img = load_img2npy(path='cafe.jpg')
    predict = model.predict_classes(img)

    print(category[predict[0]])
