import os
import pytz
from pathlib import Path
from datetime import datetime

ist = pytz.timezone('Asia/Jakarta')

def datetime_format():
    '''
    Extract daterime now to get year month day hour minute second and microsecond now
    '''
    datetime_now    = datetime.now(ist)
    year            = str(datetime_now.year)
    month           = '0'+str(datetime_now.month) if len(str(datetime_now.month)) == 1 else str(datetime_now.month)
    day             = '0'+str(datetime_now.day) if len(str(datetime_now.day)) == 1 else str(datetime_now.day)
    hour            = '0'+str(datetime_now.hour) if len(str(datetime_now.hour)) == 1 else str(datetime_now.hour)
    minute          = '0'+str(datetime_now.minute) if len(str(datetime_now.minute)) == 1 else str(datetime_now.minute)
    second          = '0'+str(datetime_now.second) if len(str(datetime_now.second)) == 1 else str(datetime_now.second)
    microsecond     = '0'+str(datetime_now.microsecond) if len(str(datetime_now.microsecond)) == 1 else str(datetime_now.microsecond)
    return year, month, day, hour, minute, second, microsecond

def get_path_save_image(sub_directory):
    '''
    Set path log in path image/yaer/month/day/sub_directory
    '''
    year, month, day, hour, _, _, _ = datetime_format()
    # path_name = f'image/{year}/{month}/{day}/{sub_directory}/'
    path_name = f'images/'
    Path(path_name).mkdir(parents=True, exist_ok=True)
    
    return path_name