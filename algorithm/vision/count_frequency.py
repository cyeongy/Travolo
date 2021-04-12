# -*- coding: utf-8 -*-

import vision_classify as vc
from collections import Counter
import os


# 학습에 사용된 카테고리 라벨
category = {1: "레포츠", 2: "인문", 3: "자연",
            11: "수상레포츠", 12: "육상레포츠", 13: "항공레포츠",
            21: "문화시설", 22: "역사관광지", 23: "휴양관광지",
            31: "자연관광지"}

# 분석서버의 이미지 저장 경로
base_path = '/home/analy/myproject/img'


# 해당 계정이 지닌 최다 빈도수의 카테고리 반환
def count_freqeuncy(*args, **kwargs):
    iidd = ""

    if "id" in kwargs:
        iidd = kwargs["id"]
    else:
        iidd = args[0]

    path = os.path.join(base_path, iidd)
    img_list = os.listdir(path=path)

    category_list = []
    for img in img_list:
        my_path = os.path.join(path, img)
        category_list.append(vc.predict(path=my_path, opt=True))

    if len(category_list) != 0:
        cnt = Counter(category_list)
        return category[cnt.most_common()[0][0]]
    else:
        return None