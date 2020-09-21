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
                    sql = "select * from analysis_tour where uid = {}".format(user_id)
                    self.analy_df = pd.read_sql_query(sql, conn)
                    sql = "select * from crawling_tour"
                    self.tour_df = pd.read_sql_query(sql, conn)
                    # print(type(float(self.tour_df['gps_lat'].iloc[0])))
                    self.tour_df.astype({'gps_lat': 'float64', 'gps_long': 'float64'})
                    sql = "select * from point"
                    self.base_df = pd.read_sql_query(sql, conn)
                    # self.base_df.astype({'gps_lat': 'float32', 'gps_long': 'float'})
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
        # if 'gps_lat' in kwargs.keys() and 'gps_long' in kwargs.keys():
        #     self.distance.set_src_gps(kwargs)
        # elif str(type(args[0])) == "<class 'dict'>" or str(type(args[0])) == "<class 'pandas.core.frame.DataFrame'>":
        #     self.distance.set_src_gps(args[0])
        # else:
        #     self.distance.set_src_gps(args[0], args[1])

    def set_dst_point(self, *args, **kwargs):
        # print("anal-args:", args)
        # print("anal-kwargs:", kwargs)

        self.distance.set_dst_gps(*args, **kwargs)
        # if 'gps_lat' in kwargs.keys() and 'gps_long' in kwargs.keys():
        #     self.distance.set_dst_gps(kwargs)
        # elif str(type(args[0])) == "<class 'dict'>" or str(type(args[0])) == "<class 'pandas.core.frame.DataFrame'>":
        #     self.distance.set_dst_gps(args[0])
        # else:
        #     self.distance.set_dst_gps(args[0], args[1])

    def get_distance(self, *args, **kwargs):
        # print("args:", args)
        # print("kwargs:", kwargs)

        if bool(args) or bool(kwargs):
            # print(bool(args) or bool(kwargs))
            self.set_dst_point(*args, **kwargs)
        return self.distance.get_distance()



