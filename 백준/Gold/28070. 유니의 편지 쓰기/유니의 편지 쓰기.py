import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    arr.append([a, b])

date_changes = {}


def increment_month(year, month):
    if month == 12:
        return year + 1, 1
    else:
        return year, month + 1


for start, end in arr:
    start_year, start_month = map(int, start.split('-'))
    end_year, end_month = map(int, end.split('-'))

    start_str = f"{start_year:04d}-{start_month:02d}"
    if start_str not in date_changes:
        date_changes[start_str] = 1
    else:
        date_changes[start_str] += 1

    end_year, end_month = increment_month(end_year, end_month)
    end_str = f"{end_year:04d}-{end_month:02d}"
    if end_str not in date_changes:
        date_changes[end_str] = -1
    else:
        date_changes[end_str] -= 1

sorted_dates = sorted(date_changes.keys())

max_value = -1
latest_date = ""
current_value = 0

for date in sorted_dates:
    current_value += date_changes[date]
    if current_value > max_value:
        max_value = current_value
        latest_date = date
    elif current_value == max_value:
        if date < latest_date:
            latest_date = date

print(latest_date)
