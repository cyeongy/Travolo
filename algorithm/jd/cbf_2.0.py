import pandas as pd
import numpy as np
import warnings;

warnings.filterwarnings('ignore')
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt
import time

start = time.time()
places = pd.read_csv('Tour_info.csv')
# print(places.shape)
places.head(1)

places_df = places[
    ['tid', 'ktop:address', 'ktop:category', 'dc:description', 'rdf:type', 'rdfs:label', 'grade', 'number of reviews']]
df_tmp1 = places_df[places_df['ktop:category'].str.contains('자연', na=False)]
df_tmp2 = places_df[places_df['ktop:category'].str.contains('인문', na=False)]
df_tmp3 = places_df[places_df['ktop:category'].str.contains('레포츠', na=False)]
df_tmp4 = places_df[places_df['ktop:category'].str.contains('쇼핑', na=False)]

places_df = pd.concat([df_tmp1, df_tmp2, df_tmp3, df_tmp4], ignore_index=True)
print(places_df)
places_df.drop_duplicates(['tid'], keep='first', inplace=True)
print("==데이터 로드성공==")
print(places_df.shape)

places_df['rdf:type'] = places_df['rdf:type'].str.replace(':', '')
#places_df['ktop:category'] = places_df['ktop:category'].str.replace(' ', '')
places_df['ktop:category'] = places_df['ktop:category'].str.replace('.', ' ')

places_df['lab'] = places_df['rdfs:label'].str.replace('(', ' ')
places_df['lab'] = places_df['rdfs:label'].str.replace(')', ' ')

places_df.astype({'dc:description': 'U'})
places_df.astype({'rdfs:label': 'U'})
places_df['dc:description'].fillna(' ')
places_df['rdfs:label'].fillna(' ')
# places_df['grade'].fillna('0')
# places_df['number of reviews'].fillna('0')
han = re.compile('[^ ㄱ-ㅎ | 가-힣 | 0-9 | a-z | A-Z ]+')
places_df['grade'].fillna(value=0.0, inplace=True)
places_df['number of reviews'].fillna(value=0.0, inplace=True)

places_df['lab'] = places_df['rdfs:label'].apply(lambda x: han.sub("", str(x)))
places_df['des'] = places_df['dc:description'].apply(lambda x: han.sub("", str(x)))
# print(places_df['rdfs:label'])
# print(places_df['lab'])
# places_df.to_json(path_or_buf='./temp.json', orient='split')
print("==데이터 전처리 작업 완료==")
okt = Okt()
print("==명사 추출 중...==")
places_df['lab'] = places_df['lab'].apply(lambda x: okt.nouns(x))
places_df['des'] = places_df['des'].apply(lambda x: okt.nouns(x))
print("==명사 추출 완료==")

print("==추출된 문자 리스트를 문자열로 변환 중...==")
places_df['lab'] = places_df['lab'].apply(lambda x: (' ').join(x))
places_df['des'] = places_df['des'].apply(lambda x: (' ').join(x))
places_df['des'] = places_df[['des', 'ktop:category']].apply(lambda x: (' ').join(x), axis=1)
places_df['lab'] = places_df[['lab', 'rdf:type']].apply(lambda x: (' ').join(x), axis=1)
print("==문자열로 재 변환 완료==")

count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))

print("==유사도 벡터화 작업 중==")
cat_mat1 = count_vect.fit_transform(places_df['des'])
cat_mat2 = count_vect.fit_transform(places_df['lab'])

cat_sim1 = cosine_similarity(cat_mat1, cat_mat1)
cat_sim2 = cosine_similarity(cat_mat2, cat_mat2)
cat_sim1 *= 0.9
cat_sim2 *= 0.1

print("==행렬화 완료!==")

cat_sim = cat_sim1 + cat_sim2
print(cat_sim.shape)
print(cat_sim)

print(time.time() - start)

place_sim_sorted_ind = cat_sim.argsort()[:, ::-1]


# print(place_sim_sorted_ind[:1])

def find_sim_pl(df, sorted_ind, tname, top_n=10):
    label = df[df['rdfs:label'] == tname]

    label_index = label.index.values
    df = df.drop(label_index)
    similar_indexes = sorted_ind[label_index, :(top_n)]

    # print(similar_indexes)
    similar_indexes = similar_indexes.reshape(-1)

    return df.iloc[similar_indexes]


print('\n명동사격장')
similar_place = find_sim_pl(places_df, place_sim_sorted_ind, '명동사격장', 50)
t = similar_place[['tid', 'rdfs:label', 'grade']].sort_values('grade', ascending=False)[:10]
print(t)

print('\n명동사격장')
similar_place = find_sim_pl(places_df, place_sim_sorted_ind, '대구 칠성시장', 50)
t = similar_place[['tid', 'rdfs:label', 'grade']].sort_values('grade', ascending=False)[:10]
print(t)
