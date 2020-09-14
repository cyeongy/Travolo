import pymysql
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from datetime import datetime
from sshtunnel import SSHTunnelForwarder

warnings.filterwarnings('ignore')

now = datetime.now()
userid = '0'
path = './'
path = path + str(now.year) + str(now.month) + str(now.minute) + str(now.second)

places = []

with SSHTunnelForwarder(('211.253.26.214', 22),
                        ssh_username='anal',
                        ssh_password='b5j4Mj6YvA9P^^',
                        remote_bind_address=('localhost', 3306)
                        ) as tunnel:
    tunnel.start()
    print(tunnel.local_bind_address, tunnel.local_bind_port)
    conn = pymysql.connect(host='localhost', port=tunnel.local_bind_port, user='client', password='cjs0701^^',
                           charset='utf8', db='jsdb')
    try:
        sql = "SELECT * FROM crawling_tour where address like '경상북도%'"
        places = pd.read_sql_query(sql, conn)
        # print(places.head())

    finally:
        conn.close()

print("=======")
places_df = places[['TID', 'address', 'category', 'description', 'label']]
# places_df.astype({'category': 'string'})
# # print(places_df)
# places_df['category'] = places_df['category'].str.replace(' ', '')
# places_df['category'] = places_df['category'].str.replace('.', ' ')
#
# # places_df['category'] = places_df['category'].str.split(', ', n=1 , expand=False)

# places_df['lit'] = places_df['category'].apply(lambda x : (' ').join(x))
count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))
cat_mat = count_vect.fit_transform(places_df['category'])
print(cat_mat.shape)
print(cat_mat)
print("=======")
cat_sim = cosine_similarity(cat_mat, cat_mat)
print(cat_sim.shape)
print("=======")
print(cat_sim)
print("=======")
place_sim_sorted_ind = cat_sim.argsort()[:, ::-1]
print(place_sim_sorted_ind[:1])
print("=======")

def find_sim_pl(df, sorted_ind, tname, top_n=10):
    label = df[df['label'] == tname]

    label_index = label.index.values
    similar_indexes = sorted_ind[label_index, : top_n]

    similar_indexes = similar_indexes.reshape(-1)
    print(similar_indexes)

    return df.iloc[similar_indexes]


similar_place = find_sim_pl(places_df, place_sim_sorted_ind, '경주', 10)
print("=======")
print(places_df.columns)
print(similar_place)
print(similar_place[['TID', 'label']])

# similar_place.to_csv(path, sep=',', na_rep='NaN')


