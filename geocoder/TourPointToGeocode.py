from Connection import ssh, connect
import pandas as pd
import numpy
import requests
import pickle

not_found_list = []
not_found_list_idx = 0
point = 0
frequency = 100

try:
    with open('./not_found_list.bin', 'rb') as f:
        not_found_list = pickle.load(f)
        t = set(not_found_list)
        not_found_list = list(t)
        not_found_list.sort()
        not_found_list_idx = len(not_found_list)
        point = pickle.load(f)
except Exception as e:
    print(e)

print(not_found_list)
print(not_found_list_idx, point)

with ssh.Tunnel() as tunnel:
    df = []

    # read sql data, make dataframe
    with connect.Connect(port=tunnel.local_bind_port) as conn:
        sql = "select * from crawling_tour"
        df = pd.read_sql_query(sql, conn)
        print(df.columns)

    # crawling basepoint geocode
    try:
        start_point = point
        while start_point < len(df.index):
            print("-----NOW CRAWLING-----", start_point)
            temp = start_point
            temp2 = start_point
            try:
                for idx in range(temp, temp + frequency):
                    if temp == len(df.index):
                        break
                    start_point += 1
                    addr = (df['address'].iloc[idx])
                    r = requests.get(
                        "http://api.vworld.kr/req/address?service=address&request=getCoord&key=2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40&&crs=epsg:4326&address=" + addr + "&refine=true&format=json&type=ROAD")
                    data = r.json()
                    result = data['response']['status']
                    if result == "OK":
                        coordinate = data['response']['result']['point']
                        df['gps_lat'].iloc[idx] = coordinate['y']
                        df['gps_long'].iloc[idx] = coordinate['x']
                        # print(df['TID'].iloc[idx], result, addr, df['gps_lat'].iloc[idx], df['gps_long'].iloc[idx], "\t",
                        #       len(not_found_list))
                    else:
                        not_found_list.append(df['TID'].iloc[idx])
                        print(df['TID'].iloc[idx], result, addr, "\t", len(not_found_list))
            except Exception as e:
                print("crawling:", e)

            print("-----NOW INSERT-----", start_point)
            try:
                with connect.Connect(port=tunnel.local_bind_port) as conn:
                    with conn.cursor() as cur:

                        if not_found_list_idx == len(not_found_list):
                            insert_key = False
                        else:
                            insert_key = True

                        for idx in range(temp2, temp2 + frequency):
                            if temp == len(df.index):
                                break
                            elif insert_key:
                                if not_found_list[not_found_list_idx] == df['TID'].iloc[idx]:
                                    not_found_list_idx += 1
                                    if not_found_list_idx == len(not_found_list):
                                        insert_key = False
                                else:
                                    sql_update = "UPDATE crawling_tour SET gps_lat = %s, gps_long = %s WHERE TID = %s "
                                    cur.execute(sql_update, (numpy.float(df['gps_lat'].iloc[idx]),
                                                             numpy.float(df['gps_long'].iloc[idx]),
                                                             numpy.int(df['TID'].iloc[idx])))
                            else:
                                sql_update = "UPDATE crawling_tour SET gps_lat = %s, gps_long = %s WHERE TID = %s "
                                cur.execute(sql_update,
                                            (numpy.float(df['gps_lat'].iloc[idx]),
                                             numpy.float(df['gps_long'].iloc[idx]),
                                             numpy.int(df['TID'].iloc[idx])))
                            # cur.execute("UPDATE crawling_tour SET 36.517907792, gps_long = 127.817000832 WHERE TID = 3")
                        # cur.execute(sql)
                        # rs = cur.fetchall()
                        # print(rs)
                        conn.commit()
                point = start_point

                with open('./not_found_list.bin', 'wb') as f:
                    pickle.dump(not_found_list, f)
                    pickle.dump(point, f)
            except Exception as e:
                print("insert:", e)

    except Exception as e:
        with open('./not_found_list.bin', 'wb') as f:
            pickle.dump(not_found_list, f)
            pickle.dump(point, f)
        print(e)

with open('./not_found_list.bin', 'wb') as f:
    pickle.dump(not_found_list, f)
    pickle.dump(point, f)

