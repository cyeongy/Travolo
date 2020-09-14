import MySQLdb, pymysql, sys, paramiko
import pandas as pd
from sshtunnel import SSHTunnelForwarder
print(sys.stdin.encoding)


ssh_public_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDSNbrI6BEa81bKovG7HLz/mTHzzhA/hsrroU8m2XhPZ/g8d+NmeSnJHuBV8H5arwQ9iJf1e/jQarRgMYGuaR8C6lyJOBiiMe/cZm6I/1OhhQjAy9OabllnAfh4rMRmG0IcmwFK4mU240Q/qh1EwhYj1l3kUgnYeaRETBvOYItX3q6/JBmE9lCNCDJgOiWpaHeOo61GlnBg12FBUztogIx/bD+Y7TGYnLjnp3x0T/OjJWDZj4FNny3/co8ayxz0fxxOZPXjVWSaeS85RjeHHnPZO+6nMdB/NRef3pnAPgWOMBzk9BisiLpWozxDiCYr1Yuwq5SCLCdxULal+7VYzWM9 anal@root'
ssh_private_key='MIIEpAIBAAKCAQEA0jW6yOgRGvNWyqLxuxy8/5kx884QP4bK66FPJtl4T2f4PHfjZnkpyR7gVfB+Wq8EPYiX9Xv40Gq0YDGBrmkfAupciTgYojHv3GZuiP9ToYUIwMvTmm5ZZwH4eKzEZhtCHJsBSuJlNuNEP6odRMIWI9Zd5FIJ2HmkREwbzmCLV96uvyQZhPZQjQgyYDolqWh3jqOtRpZwYNdhQVM7aICMf2w/mO0xmJy456d8dE/zoyVg2Y+BTZ8t/3KPGssc9H8cTmT141VkmnkvOUY3hx5z2TvupzHQfzUXn96ZwD4FjjAc5PQYrIi6VqM8Q4gmK9WLsKuUgiwncVC2pfu1WM1jPQIDAQABAoIBAE2ZWg+KY64gQFzjk/rv2/E7G06WNjdNSiF71d1QkHI3vlKMK10Lw1okVMpE0lAlpZoVj4smra46hcWw4N+CnNkVrP1WwPk3GAWzpoBaSQQqORX66G1s6QH2n0Pk+0d6Loiiy/JZ6uU9NleOM+nLACNQoi6D/nB0TyiLNASWbToNJfTPI9xFe5OWZ5cVyMHeLhIAc2pt4MmdI4osegoVssNN21iWLluyN7HxeajMiAgmh1liiG3skDpsjHg8hLiBv6Bxnu1Fny+mrGxVf810jsRxgZkTThlzg35B9YjyPDv2htbxp62AGFjtxh/PDcDQm4u5/SgnVcqgmIfISnIOlwECgYEA7+OHpI21mBmizFOF8KntVJo+jUoUivRrvaxubTUiSNejkzdw08mq7Ur3+PMOKRM4509/xOYXiZ8P13jSMMlI8E4a4aypFk1zjsRkmjp/ELX5ES4BgWPcA/ldNB1/GWB91wz7jiKgGMelog31nTwMwaOr0RMcZbhP7JW+umhfsf0CgYEA4FPsMUrVQXMcT1CyeSsLxtcUG6YwvmolbbqK9zV6CuKfF2tXngIRjp4/94ofUXsKVKchWzJ+vcsn8sk1fe4AuRKXxokOLjmowGRE4PVXi+4AUTKp3kcxBq4I5XDjSh6ewzLUYJovghFKdK5Lsic9EPxxn1P3rym5d8Q7j1TbmkECgYBj4kFgawDpzALVQRHMG3UOfQr+mZHkKdGSsHFqV21nFyKs8bCw/o+FLmoB5nJG+BIBfkCdI5E5ZFmcRlp+pdEQ/fSDcvkUqDstfujErwapVpvWY2mNDp9VqEb+pCl/z4WWPXmgvRocN0ToLRfP2GkXV6b67xIr6Iqe39sCkuMFoQKBgQDRE0aqtl1F79wtzD9bERSb0S9riZwajGGwAFGuj8fcR1URhbkWikUE0Fc8Bh6kWXHKbi53ift4NtVXwdI6OU2xMDQHFQwDZzfxgEJ2DBP5VewzwW1yvpVh7WhbN7iPBzTfJwursWif6C+lyiDAvTN8Flxrq93IArJafqkoMGWwQQKBgQDcEhomrFANZcXcTEwGaztydCSmgER7r0gHSzpQbtFpSObWb+YCq8qZgZTTWZWlfTPXFEgEEBGOgCL8tqMhPGMdYvWsmnlzrAmI00FyWmyA07lv9JLkip9bZtbcYJ/GR8nsVz/yFeewAGXrrGzy14D5qEj4fgYQYwtSjPFKqe5XzA=='

with SSHTunnelForwarder(('211.253.26.214', 22),
                        ssh_username='anal',
                        ssh_password='b5j4Mj6YvA9P^^',
                        remote_bind_address=('localhost', 3306)
                        ) as tunnel:
    tunnel.start()
    print(tunnel.local_bind_address, tunnel.local_bind_port)
    conn = pymysql.connect(host='localhost', port=tunnel.local_bind_port, user='client', password='cjs0701^^', charset='utf8', db='jsdb')
    try:
        # with conn.cursor() as cur:
        #     sql = "select address from crawling_tour"
        #     cur.execute(sql)
        #     result = cur.fetchall()
        #     for temp in result:
        #         print(temp)
        sql = "select address from crawling_tour"
        df = pd.read_sql_query(sql, conn)
        print(len(df.index))

    finally:
        conn.close()



    # with pymysql.connect(host='211.253.26.214', user='client', password='cjs0701^^', port=22, charset='utf8', database='jsdb') as conn:
    #     with conn.cursor() as cur:
    #
    #         cur.execute("select * from client")
    #         result = cur.fetchall()
    #         for temp in result:
    #             print(temp[0])
