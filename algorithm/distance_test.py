import pymysql, requests, numpy
import pandas as pd
import math
from sshtunnel import SSHTunnelForwarder



with SSHTunnelForwarder(('211.253.26.214', 22),
                        ssh_username='anal',
                        ssh_password='b5j4Mj6YvA9P^^',
                        remote_bind_address=('localhost', 3306)
                        ) as tunnel:
    print(tunnel.local_bind_address, tunnel.local_bind_port)
    conn = pymysql.connect(host='localhost', port=tunnel.local_bind_port, user='client', password='cjs0701^^', charset='utf8', db='jsdb')

    sql = "select tid, address, gps_lat, gps_long from crawling_tour limit 3"
    sql_distance = "SELECT (6371*acos(cos(radians( {A_LAT} ))*cos(radians( {B_LAT} ))*cos(radians( {B_LONG} )-radians( {A_LONG} ))+sin(radians( {A_LAT} ))*sin(radians( {B_LAT} )))) AS distacne FROM crawling_tour HAVING distance <= 30 ORDER BY distance"

    # A_LAT, B_LAT, B_LONG, A_LONG, A_LAT, B_LAT
    df = pd.read_sql_query(sql, conn)

    A_LAT = 37.711580904
    A_LONG = 128.600402264
    B_LAT = numpy.float(df['gps_lat'].iloc[1])
    B_LONG = numpy.float(df['gps_long'].iloc[1])

    try:
        result = 6371 * math.acos(math.cos(math.radians(A_LAT)) * math.cos(math.radians(B_LAT)) * math.cos(math.radians(B_LONG) - math.radians(A_LONG)) + math.sin(math.radians(A_LAT)) * math.sin(math.radians(B_LAT)))
        print(result)
    except Exception as e:
        print(e)

    with conn.cursor() as cursor:
        for idx in range(len(df.index)):
            sql_distance= "SELECT (6371*acos(cos(radians( {A_LAT} ))*cos(radians( {B_LAT} ))*cos(radians( {B_LONG} )-radians( {A_LONG} ))+sin(radians( {A_LAT} ))*sin(radians( {B_LAT} )))) AS distacne FROM crawling_tour HAVING distance <= 30 ORDER BY distance".format(A_LAT='37.711580904', A_LONG='128.600402264', B_LAT=df['gps_lat'].iloc[idx], B_LONG=df['gps_long'].iloc[idx])
            print(sql_distance)
    print(df.head())

