from algorithm.distance import GPSDistance as dis
from algorithm.Analysis import AnalysisCBF as anal
import pandas as pd


a = anal(12)
# 37.711580904, 128.600402264
# gps_lat=37.711580904, gps_long=128.600402264
# base['gps_lat'], base['gps_long']
# test = a.tour_df.iloc[0]
# print(test)
base = {'gps_lat': 37.711580904, 'gps_long': 128.600402264, 'trash': ["fuck you error"]}
base_df = pd.DataFrame({'gps_lat': [37.711580904], 'gps_long': [128.600402264], 'trash': ["fuck you error"]})
anal_src = a.tour_df.iloc[0]
anal_dst = a.tour_df.iloc[3]
# print(anal_src[['gps_lat', 'gps_long']], anal_dst[['gps_lat', 'gps_long']], sep="\n")
print(anal_src)

print("------base-----")
# a.set_base_gps(37.711580904, 128.600402264)
a.set_src_point(anal_src)
print("------dst-----")
a.set_dst_point(anal_dst)

print("------res-----")
dst = {'gps_lat': 35.767944611, 'gps_long': 128.132317657}
dst_df = pd.DataFrame(anal_dst)
# gps_lat=35.767944611, gps_long=128.132317657
# dst['gps_lat'], dst['gps_long']
print(a.get_distance())

# for i in range(5):
#     print(i)
#
# t = anal(12)
#
# for i in t.pick_data():
#     print(i['TID'])
#     print()
#
#


