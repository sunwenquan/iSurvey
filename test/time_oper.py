import time,datetime
import pytz
from tzlocal import get_localzone # $ pip install tzlocal
# 1. 如何设置时区
# set timezone
tz = pytz.timezone('Asia/Shanghai')
# get local timezone  
local_tz = get_localzone() 
# get all_timezones 
all_timezones = pytz.all_timezones 
print(all_timezones)
print(tz)
print(local_tz)
# 2. 获取时间
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
