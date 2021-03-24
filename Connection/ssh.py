from sshtunnel import SSHTunnelForwarder


# with SSHTunnelForwarder(('211.253.26.214', 22),
#                         ssh_username='anal',
#                         ssh_password='b5j4Mj6YvA9P^^',
#                         remote_bind_address=('localhost', 3306)
#                         ) as tunnel:
#     tunnel.start()

class Tunnel:
    def __init__(self):
        self.tunnel = SSHTunnelForwarder(('211.253.26.214', 22),
                                         ssh_username='analy',
                                         ssh_password='b5j4Mj6YvA9P^^',
                                         remote_bind_address=('localhost', 3306)
                                         )

    def __enter__(self):
        # print("ssh tunnel start")
        self.tunnel.start()
        return self.tunnel

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("ssh tunnel closed")
        self.tunnel.close()
