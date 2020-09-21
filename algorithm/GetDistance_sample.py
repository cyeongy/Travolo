from algorithm.Analysis import AnalysisCBF as anal
import pandas as pd

a = anal(user_id=12)

anal_src = a.tour_df.iloc[0]
anal_dst = a.tour_df.iloc[1]

# 출발 포인트 설정
a.set_src_point(anal_src)

# 도착 포인트 설정
a.set_dst_point(anal_dst)
print(a.get_distance())

# 도착 포인트 사전 설정 없이 얻기
a.set_dst_point(a.tour_df.iloc[2])
print(a.get_distance(anal_dst))