import Analysis as analy
from multiprocessing import shared_memory
import pandas as pd
import time

def make_tourList(base_point, user_id, range = 20.0):

    place_sim_sorted_ind = shared_memory.SharedMemory(name='CBF_Matrix')
    item_sim_df = pd.read_csv('item_sim.csv')

    a = analy.AnalysisCBF(user_id)

    cat_sim.close()
    time.sleep(5)

    anal_src = a.base_df[a.base_df['base_address'] == base_point]
    # 출발 포인트 설정
    a.set_src_point(anal_src)

    # print(a.analy_df)

    def find_sim_pl(df, sorted_ind, tid, top_n=10):

        place = df[df['TID'] == tid]

        place_index = place.index.values
        # df = df.drop(place_index)
        similar_indexes = sorted_ind[place_index, :(top_n)]

        # print(similar_indexes)
        similar_indexes = similar_indexes.reshape(-1)

        return df.iloc[similar_indexes]

    result_df = pd.DataFrame(columns=['TID', 'label', 'address', 'category', 'grade', 'vote_count'])

    for i in a.analy_df['TID']:
        similar_place = item_sim_df[f'{i}'].sort_values(ascending=False)[1:50]
        #print(type(similar_place))
        #print(similar_place)

        for l in similar_place.index:
            anal_dst = a.tour_df[a.tour_df['TID'] == l]
            # print("====anal_dst====")
            # print(anal_dst)

            a.set_dst_point(anal_dst)

            if a.get_distance() <= range:
                result_df = result_df.append(anal_dst, ignore_index=True)

        similar_place = find_sim_pl(a.tour_df, place_sim_sorted_ind, i, 25)

        for j in similar_place['TID']:
            anal_dst = a.tour_df[a.tour_df['TID'] == j]
            # print("====anal_dst====")
            # print(anal_dst)

            a.set_dst_point(anal_dst)

            if a.get_distance() <= range:
                result_df = result_df.append(anal_dst,ignore_index=True)

            # print(result_df)

    result_df = result_df.drop_duplicates(['label'])
    result_df = result_df[result_df['category'].str.contains('자연|인문|레포츠|쇼핑', na=False)]
    t = result_df.sort_values('grade', ascending=False)[:50]

    t = t.sample(frac=1).reset_index(drop=True)

    #print(f'종료합니다 소요시간 : {time.time() - start}')

    return t
