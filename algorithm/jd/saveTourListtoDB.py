import connect
import time
import pandas as pd

def save(df, base_address):
    try:
        with connect.Connect() as conn:
            cur = conn.cursor()
            now = time.strftime('%y%m%d%H%M%S', time.localtime(time.time()))
            group_no = f"{now}"
            x=0
            print("UID | TID | SCHEDULE_NAME | DATE | GROUP_NO | TIME")
            while x < len(df.index):
                sql = f"insert into schedule (UID, TID, SCHEDULE_NAME, DATE, GROUP_NO, TIME) value ({df.loc[x]['UID']},{df.loc[x]['TID']},'{base_address}','{df.loc[x]['DATE']}','{group_no}',{df.loc[x]['TIME']})"
                cur.execute(sql)
                conn.commit()
                x += 1
    except Exception as e:
        print(e)

        return -1

    finally:
        return 1
