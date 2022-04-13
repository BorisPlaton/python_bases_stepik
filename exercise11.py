import datetime

print(next(map(lambda x: f"{x.year} {x.month} {x.day}", [datetime.date(*map(int, input().split())) + datetime.timedelta(int(input()))])))
