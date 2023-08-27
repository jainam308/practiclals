from datetime import date,timedelta
def all_sunday(year):
    d=date(year,1,1)
    d+=timedelta(days=6-d.weekday())
    while d.year == year:
        yield d
        d+=timedelta(days=7)
for d in all_sunday(2022):
    print(d)
