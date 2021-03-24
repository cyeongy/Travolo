import pymysql


class Connect:
    def __init__(self, port=3306):
        self.conn = pymysql.connect(host='localhost',
                                    port=port,
                                    user='analy',
                                    password='ajs0701^^',
                                    charset='utf8',
                                    db='jsdb')

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
