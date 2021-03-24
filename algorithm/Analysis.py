import pandas as pd
from Connection import ssh, connect
import random
from algorithm.distance import GPSDistance


# TOUR_NO | UID | TID   | GRADE
class AnalysisCBF:
    pick_number = 4
    distance = GPSDistance()

    # get uid and get analysis data from table
    def __init__(self, user_id=12):
        try:
            with ssh.Tunnel() as tunnel:
                with connect.Connect(port=tunnel.local_bind_port) as conn:
                    sql1 = "select * from analysis_tour where uid = {}".format(user_id)
                    self.analy_df = pd.read_sql_query(sql1, conn)
                    self.analy_df.drop_duplicates(['TID'], inplace=True)

                    sql2 = "select * from crawling_tour"
                    self.tour_df = pd.read_sql_query(sql2, conn)

                    sql3 = "select * from point"
                    self.base_df = pd.read_sql_query(sql3, conn)
        except Exception as e:
            print(e)

    # pick number of random data (default number == 4)
    def pick_data(self, number=pick_number):
        arr = [i for i in range(len(self.analy_df.index))]
        random.shuffle(arr)

        # list 범위를 초과하는 숫자 차단
        endpoint = number if number <= len(self.analy_df.index) else len(self.analy_df.index)

        # print(arr)
        # print(arr[:number])

        for i in arr[:endpoint]:
            # print(self.df.iloc[i])
            yield self.analy_df.iloc[i]

    def CBF(self):
        pass

    def set_src_point(self, *args, **kwargs):
        # print("anal-args:", args)
        # print("anal-kwargs:", kwargs)

        self.distance.set_src_gps(*args, **kwargs)

    def set_dst_point(self, *args, **kwargs):
        # print("anal-args:", args)
        # print("anal-kwargs:", kwargs)

        self.distance.set_dst_gps(*args, **kwargs)

    def get_distance(self, *args, **kwargs):
        # print("args:", args)
        # print("kwargs:", kwargs)

        if bool(args) or bool(kwargs):
            # print(bool(args) or bool(kwargs))
            self.set_dst_point(*args, **kwargs)
        return self.distance.get_distance()

    def get_route(self, tour_list):
        result = []
        temp = self.tour_df[['TID', 'gps_lat', 'gps_long']]
        temp.set_index('TID', inplace=True)

        distance = [[1000 for i in range(len(tour_list))] for j in range(len(tour_list))]
        visited = [False for i in range(len(tour_list))]
        check = [True for i in range(len(tour_list))]

        for i in range(len(tour_list)):
            self.set_src_point(temp.loc[tour_list[i]])
            for j in range(len(tour_list)):
                if i == j:
                    continue
                distance[i][j] = self.get_distance(temp.loc[tour_list[j]])

        now = 0
        while not check == visited:
            result.append(tour_list[now])
            visited[now] = True
            ok = True
            while ok:
                if check == visited:
                    break
                pick = distance[now].index(min(distance[now]))
                if visited[pick]:
                    distance[now][pick] = 1000
                else:
                    ok = False

            now = pick

        return result
