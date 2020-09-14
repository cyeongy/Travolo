import pymysql, requests, numpy
import pandas as pd
from sshtunnel import SSHTunnelForwarder

pkey = '2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40'
not_found_list = []
not_found_list_idx = 0

with SSHTunnelForwarder(('211.253.26.214', 22),
                        ssh_username='anal',
                        ssh_password='b5j4Mj6YvA9P^^',
                        remote_bind_address=('localhost', 3306)
                        ) as tunnel:
    print(tunnel.local_bind_address, tunnel.local_bind_port)
    conn = pymysql.connect(host='localhost', port=tunnel.local_bind_port, user='client', password='cjs0701^^', charset='utf8', db='jsdb')



    sql = "select tid, address, gps_lat, gps_long from crawling_tour"
    df = pd.read_sql_query(sql, conn)

    conn.close()
    # print(df.columns)
    # print(df.head())
    # print(df.iloc[1])
    print(len(df.index))
    start_point = 19300
    try:
        while start_point != len(df.index):
            print("-----NOW CRAWLING-----")
            temp = start_point
            temp2 = start_point
            for idx in range(temp, temp+1000):
                if temp == len(df.index):
                    break
                start_point += 1
                addr = (df['address'].iloc[idx])
                r = requests.get("http://api.vworld.kr/req/address?service=address&request=getCoord&key=2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40&&crs=epsg:4326&address="+addr+"&refine=true&format=json&type=ROAD")
                data = r.json()
                result = data['response']['status']
                if result == "OK":
                    coordinate = data['response']['result']['point']
                    df['gps_lat'].iloc[idx] = coordinate['y']
                    df['gps_long'].iloc[idx] = coordinate['x']
                    print(df['tid'].iloc[idx], result, addr, df['gps_lat'].iloc[idx], df['gps_long'].iloc[idx], "\t", len(not_found_list))
                else:
                    not_found_list.append(df['tid'].iloc[idx])
                    print(df['tid'].iloc[idx], result, addr, "\t", len(not_found_list))

            print("-----NOW INSERT-----")
            try:
                conn = pymysql.connect(host='localhost', port=tunnel.local_bind_port, user='client', password='cjs0701^^', charset='utf8', db='jsdb')
                with conn.cursor() as cur:

                    insert_key = True
                    for idx in range(temp2, temp2+1000):
                        if temp == len(df.index):
                            break
                        elif insert_key:
                            if not_found_list[not_found_list_idx] == df['tid'].iloc[idx]:
                                not_found_list_idx += 1
                                if not_found_list_idx == len(not_found_list):
                                    insert_key = False
                            else:
                                sql_update = "UPDATE crawling_tour SET gps_lat = %s, gps_long = %s WHERE TID = %s "
                                cur.execute(sql_update, (numpy.float(df['gps_lat'].iloc[idx]),
                                                         numpy.float(df['gps_long'].iloc[idx]),
                                                         numpy.int(df['tid'].iloc[idx])))
                        else:
                            sql_update = "UPDATE crawling_tour SET gps_lat = %s, gps_long = %s WHERE TID = %s "
                            cur.execute(sql_update,
                                        (numpy.float(df['gps_lat'].iloc[idx]),
                                         numpy.float(df['gps_long'].iloc[idx]),
                                         numpy.int(df['tid'].iloc[idx])))
                        # cur.execute("UPDATE crawling_tour SET 36.517907792, gps_long = 127.817000832 WHERE TID = 3")
                    # cur.execute(sql)
                    # rs = cur.fetchall()
                    # print(rs)
                conn.commit()
            except Exception as e:
                print(e)
            finally:
                conn.close()
    except Exception as e:
        print(e)

print(not_found_list)