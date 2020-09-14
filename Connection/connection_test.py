import Connection.connect as con
import pandas as pd
from sshtunnel import SSHTunnelForwarder
from Connection.ssh import Tunnel


# with SSHTunnelForwarder(('211.253.26.214', 22),
#                         ssh_username='anal',
#                         ssh_password='b5j4Mj6YvA9P^^',
#                         remote_bind_address=('localhost', 3306)
#                         ) as tunnel:

with Tunnel() as tunnel:
    with con.Connect(port=tunnel.local_bind_port) as conn:
        print(tunnel.local_bind_port)
        try:
            sql = "select tid, address from crawling_tour limit 3"
            data = pd.read_sql_query(sql, conn)
            print(data.head())

        except Exception as e:
            print(e)