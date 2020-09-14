from Connection import ssh, connect
import pandas as pd


# 'pid', 'base_address', 'gps_lat', 'gps_long'

with ssh.Tunnel() as tunnel:
    df = []
    # read sql data, make dataframe
    with connect.Connect(port=tunnel.local_bind_port) as conn:
        sql = "select * from point"
        df = pd.read_sql_query(sql, conn)
        print(df.columns)