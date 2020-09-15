from sshtunnel import SSHTunnelForwarder


class Tunnel:
    def __init__(self):
        self.tunnel = SSHTunnelForwarder(('127.0.0.1', 22),
                                         ssh_username='anal',
                                         ssh_password='ssh_password',
                                         remote_bind_address=('localhost', 3306)
                                         )

    def __enter__(self):
        # print("ssh tunnel start")
        self.tunnel.start()
        return self.tunnel

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("ssh tunnel closed")
        self.tunnel.close()
