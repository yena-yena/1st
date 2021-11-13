import datetime as dt
loveday = dt.datetime(2019, 2, 24)
print("춘향이와 몽룡이의 연애 시작일 : {}년 {}월 {}일".format(loveday.year, loveday.month, loveday.day))
hundred = dt.timedelta(days=100)
two_hundred = dt.timedelta(days=200)
five_hundred = dt.timedelta(days=500)
thousand = dt.timedelta(days=1000)

anniversary100 = loveday + hundred
anniversary200 = loveday + two_hundred
anniversary500 = loveday + five_hundred
anniversary1000 = loveday + thousand

print("100일 기념일 : {}년 {}월 {}일".format(anniversary100.year, anniversary100.month, anniversary100.day))
print("200일 기념일 : {}년 {}월 {}일".format(anniversary200.year, anniversary200.month, anniversary200.day))
print("500일 기념일 : {}년 {}월 {}일".format(anniversary500.year, anniversary500.month, anniversary500.day))
print("1000일 기념일 : {}년 {}월 {}일".format(anniversary1000.year, anniversary1000.month, anniversary1000.day))
