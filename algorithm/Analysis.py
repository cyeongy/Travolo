import pandas as pd
from Connection import ssh, connect
import random
from algorithm.distance import GPSDistance


# TOUR_NO | UID | TID   | GRADE
class AnalysisCBF:

    pick_number = 4

    # get uid and get analysis data from table
    def __init__(self, uid):
        try:
            with ssh.Tunnel() as tunnel:
                with connect.Connect(port=tunnel.local_bind_port) as conn:
                    sql = "select * from analysis_tour where uid = {}".format(uid)
                    self.analy_df = pd.read_sql_query(sql, conn)
                    sql = "select * from crawling_tour"
                    self.tour_df = pd.read_sql_query(sql, conn)
                    sql = "select * from point"
                    self.base_df = pd.read_sql_query(sql, conn)
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



