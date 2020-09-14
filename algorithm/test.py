from algorithm.distance import GPSDistance as dis
from algorithm.Analysis import AnalysisCBF as anal
import pandas as pd

def test(a):
    print(a)


a = dis()
# 37.711580904, 128.600402264
# gps_lat=37.711580904, gps_long=128.600402264
# base['gps_lat'], base['gps_long']
base = {'gps_lat': [37.711580904], 'gps_long': [128.600402264], 'trash':["fuck you error"]}
df = pd.DataFrame(base)
print(type(df))
print(df.head())


print("------base-----")
a.set_base_gps(df)
# a.set_base_gps(37.711580904, 128.600402264)

print("------dest-----")

a.set_dest_gps(35.767944611, 128.132317657)



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
