import tourListing
from algorithm.jd import saveTourListtoDB as sd
import pandas as pd
import datetime


def tourList_run(base_address, user_id, start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    days = (end_date - start_date).days + 1
    numOfoneday = 4
    range = 20

    tmp_df = tourListing.make_tourList(base_address, user_id, range)
    while len(tmp_df.index) < days * 3:
        range += 10
        tmp_df = tourListing.make_tourList(base_address, user_id, range)

    # print(result.head(days*3))

    tmp_df = tmp_df.head(days * numOfoneday)
    result_df = pd.DataFrame(columns=['TID', 'UID', 'DATE', 'TIME'])

    x = 0
    y = 0
    while x < (days * numOfoneday):
        result_df.loc[x] = [tmp_df.loc[x]['TID'], user_id,
                            datetime.datetime.strftime((start_date + datetime.timedelta(days=y)), '%Y-%m-%d'), x]
        x += 1
        if x % numOfoneday == 0:
            y += 1

    # print(result_df)
    issuc = sd.save(result_df, base_address)

    if issuc == 1:
        print('일정 생성 완료')
    else:
        print('생성 실패')
