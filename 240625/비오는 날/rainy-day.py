import datetime

n = int(input())
data = []

for _ in range(n):
    date, day, weather = input().split()
    data.append((datetime.datetime.strptime(date, "%Y-%m-%d").date(), day, weather))

earliest_rain_date = None
earliest_rain_index = None

for i, (date, day, weather) in enumerate(data):
    if weather == "Rain":
        if earliest_rain_date is None or date < earliest_rain_date:
            earliest_rain_date = date
            earliest_rain_index = i

if earliest_rain_index is not None:
    print(f"{data[earliest_rain_index][0]} {data[earliest_rain_index][1]} {data[earliest_rain_index][2]}")
else:
    print("No rain day")