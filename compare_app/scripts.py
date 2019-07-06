from datetime import datetime
import numpy as np
import pandas as pd



"""
from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

"""

global_path = "D:\\programming\\hack\\hack\\static\\tsj.csv"

def getAverageWorkTime(works):
    time_list = []
    for work in works:
        if work['status'] == 'done':
            time_delta = datetime.strptime(work['challenge_done'], '%Y-%M-%d') - datetime.strptime(work['challenge_accepted'], '%Y-%M-%d')
            time_list.append(time_delta.days)
    return np.round(np.array(time_list).mean(), 1)

def getCompareObjectsForWorkTime(f_works, s_works):
    f_time = getAverageWorkTime(f_works)
    s_time = getAverageWorkTime(s_works)
    return {'first': f_time, 'second': s_time}

def getPercentOfReasonToCall(works):
    count = 0
    if len(works)!=0:
        for work in works:
            if work['status'] == 'done':
                count += 1
        print(count, len(works))
        return count/len(works)*100
    else:
        return 0

def getCompareObjectsOfReasonToCall(f_works, s_works):
    f_percent = getPercentOfReasonToCall(f_works)
    s_percent = getPercentOfReasonToCall(s_works)
    return {'first': f_percent, 'second': s_percent}

def getWorksOnPeriod(works, start_period, end_period):
    res = {'works': []}
    for work in works:
        time = datetime.strptime(work['challenge_accepted'], '%Y-%d-%M')
        start = datetime.strptime(start_period, '%Y-%d-%M')
        end = datetime.strptime(end_period, '%Y-%d-%M')
        if time >= start and time <= end:
            res['works'].append(work)
    return res

def getGlobalRating(tsj_id):
    df = pd.read_csv(global_path, delimiter = ',')
    return float(df[df['id']==tsj_id]['w_summ'])

def getTotalHouses(tsj_id):
    df = pd.read_csv(global_path, delimiter = ',')
    return float(df[df['id']==tsj_id]['count_mkd'])

def getTotalSquares(tsj_id):
    df = pd.read_csv(global_path, delimiter = ',')
    return float(df[df['id']==tsj_id]['area_total'])

def getCompareObjectsOfGlobalRating(f_id, s_id):
    f_rating = getGlobalRating(f_id)
    s_rating = getGlobalRating(s_id)
    return {'first': f_rating, 'second': s_rating}

def getCompareObjectsOfTotalHouses(f_id, s_id):
    f_houses = getTotalHouses(f_id)
    s_houses = getTotalHouses(s_id)
    return {'first': f_houses, 'second': s_houses} 

def getCompareObjectsOfTotalSquares(f_id, s_id):
    f_sq = getTotalSquares(f_id)
    s_sq = getTotalSquares(s_id)
    return {'first': f_sq, 'second': s_sq} 


def getCompareObjectsOfTotalHouses(f_id, s_id):
    f_houses = getTotalHouses(f_id)
    s_houses = getTotalHouses(s_id)
    return {'first': f_houses, 'second': s_houses} 








