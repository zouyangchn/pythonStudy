from datetime import datetime, timedelta, timezone

now = datetime.now() # 获取当前datetime
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


dt = datetime(2019, 11, 19, 12, 50)
print(dt)
print(dt.timestamp())

ts=datetime.now().timestamp()
print(datetime.fromtimestamp(ts))
print(datetime.utcfromtimestamp(ts))


cday = datetime.strptime('2019-11-21 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


now = datetime.now()
print( now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
print(tz_utc_8)
now=datetime.now()
print(now)
print(now.replace(tzinfo=tz_utc_8))

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


