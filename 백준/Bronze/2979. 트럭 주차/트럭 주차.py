import sys

ans = 0

A, B, C = map(int, sys.stdin.readline().rstrip().split())

parks = []

times = [0] * 100

for _ in range(3):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    for i in range(start, end):
        times[i] += 1

for time in times:
    if time == 1:
        ans += A
    elif time == 2:
        ans += (2 * B)
    elif time == 3:
        ans += (3 * C)

print(ans)
