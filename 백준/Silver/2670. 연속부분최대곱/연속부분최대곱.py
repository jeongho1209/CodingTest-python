import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(n):
    arr.append(float(sys.stdin.readline().rstrip()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])

print('%0.3f' % max(arr))
