import sys

arr = []
w, q = 0, 0

for _ in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

SUM = sum(arr)

arr.sort()

for i in range(8):
    for j in range(i + 1, 9):
        if SUM - arr[i] - arr[j] == 100:
            w = arr[i]
            m = arr[j]

for i in arr:
    if i == w or i == m:
        continue
    print(i)
