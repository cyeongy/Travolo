from Connection import ssh, connect
import pandas as pd
import numpy
import requests
import pickle

# 'pid', 'base_address', 'gps_lat', 'gps_long'
not_found_list = []
not_found_list_index = 0

with ssh.Tunnel() as tunnel:
    df = []

    # read sql data, make dataframe
    with connect.Connect(port=tunnel.local_bind_port) as conn:
        sql = "select pid, base_address from point"
        df = pd.read_sql_query(sql, conn)
        print(df.columns)
        df['gps_lat'] = 0.0
        df['gps_long'] = 0.0

    # crawling basepoint geocode
    print("-----NOW CRAWLING-----")
    for idx in range(len(df.index)):
        addr = (df['base_address'].iloc[idx])
        r = requests.get(
            "http://api.vworld.kr/req/address?service=address&request=getCoord&key=2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40&&crs=epsg:4326&address=" + addr + "&refine=true&format=json&type=ROAD")
        data = r.json()
        result = data['response']['status']

        if result == "OK":
            coordinate = data['response']['result']['point']
            df['gps_lat'].iloc[idx] = coordinate['y']
            df['gps_long'].iloc[idx] = coordinate['x']
            print(df['pid'].iloc[idx], result, addr, df['gps_lat'].iloc[idx], df['gps_long'].iloc[idx], "\t",
                  len(not_found_list))
        else:
            not_found_list.append(df['pid'].iloc[idx])
            print(df['pid'].iloc[idx], result, addr, "\t", len(not_found_list))

    # insert data into mysql
    print("-----NOW INSERT-----")
    with connect.Connect(port=tunnel.local_bind_port) as conn:
        try:
            with conn.cursor() as cur:
                for idx in range(len(df.index)):
                    sql_update = "UPDATE point SET gps_lat = %s, gps_long = %s WHERE pid = %s "
                    print(df.iloc[idx])
                    cur.execute(sql_update, (numpy.float(df['gps_lat'].iloc[idx]),
                                             numpy.float(df['gps_long'].iloc[idx]),
                                             numpy.int(df['pid'].iloc[idx])))
                    conn.commit()

        except Exception as e:
            print(e)


# 에러 발생시 여태까지 기록해둔 미확인 주소 기록
with open('./not_found_base.bin', 'wb') as f:
    pickle.dump(not_found_list, f)
