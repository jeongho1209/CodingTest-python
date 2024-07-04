import sys

arr = []

max_len = 0

for _ in range(5):
    arr.append(list(sys.stdin.readline().rstrip()))

for i in arr:
    if len(i) > max_len:
        max_len = len(i)

for i in range(5):
    for index in range(max_len):
        try:
            arr[i][index]
        except:
            arr[i].append('*')

result = ''

for i in range(max_len):
    for index in range(5):
        result += arr[index][i]

print(result.replace('*', ''))