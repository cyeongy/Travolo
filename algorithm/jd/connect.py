with connect.Connect(port=tunnel.local_bind_port) as conn:
    sql = "select * from analysis_tour"
    a_df = pd.read_sql_query(sql, conn)
    sql = "select * from crawling_tour"
    t_df = pd.read_sql_query(sql, conn)

    print("==Data Frame Ready==")

    #ratings_matrix = a_df.pivot_table('GRADE',index='UID',columns='TID')
    #print(ratings_matrix.head(3))

    rating_place = pd.merge(a_df, t_df, on='TID')
    ratings_matrix = rating_place.pivot_table('GRADE', index='UID', columns='TID')
    ratings_matrix = ratings_matrix.fillna(0)

    ratings_matrix_T = ratings_matrix.transpose()
    print("==Matrix Ready==")
    #print(ratings_matrix_T.head(3))

    item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)

        # cosine_similarity() 로 반환된 넘파이 행렬을 영화명을 매핑해 Dataframe으로 변환

    item_sim_df = pd.DataFrame(data=item_sim, index=ratings_matrix.columns, columns=ratings_matrix.columns)
    print("==Similarity sort ok==")
    item_sim_df.to_csv('item_sim.csv', mode='w', encoding='utf-8-sig')