# 파이썬에서 날짜와 시간을 다루는 방법
import datetime

# 현재시간
now = datetime.datetime.now()
print(now)

# 문자열 포맷팅
# stringifytime
nowdate = now.strftime('%Y-%m-%d')
print(nowdate)

nowdate = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowdate)

# 문자열 -> datetime
strdatetime = '2017-10-16 12:23:40'
# string print time
datetime1 = datetime.datetime.strptime(strdatetime, '%Y-%m-%d %H:%M:%S')
print(type(datetime1))
print(datetime1)

# 날짜나 시간 변경
datetime2 = datetime1.replace(day=20)
print(datetime1)
print(datetime2)

# 날짜만 관리하기 위한 datetime.date
# 시간만 관리하기 위한 datetime.time
d = datetime.date(2015, 1, 1)
t = datetime.time(6, 0, 0)
print(d, t)

# date와 time을 합치기
dt = datetime.datetime.combine(d, t)
print(type(dt))
print(dt)

# datetime에서 년, 월, 일, 시, 분, 초 각각 접근하기
t = dt.timetuple()
print(t)
print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


# 날짜, 시간 더하기
# 1주 더하기 datetime.timedelta(weeks=1)
# 1일 더하기 datetime.timedelta(days=1)
# 1시간 더하기 datetime.timedelta(hours=1)
# 1분 더하기 datetime.timedelta(minutes=1)
# 1초 더하기 datetime.timedelta(seconds=1)
# 1밀리세컨드 더하기 datetime.timedelta(milliseconds=1)
now = datetime.datetime.now()
print(now)
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)

# datetime에서 datetime 빼기
dt1 = datetime.datetime.strptime('2017-10-16', '%Y-%m-%d')
dt2 = datetime.datetime.strptime('2017-10-17', '%Y-%m-%d')
dt3 = dt2 - dt1
print(dt1)
print(dt2)
print(dt3)
print(dt3.days)
