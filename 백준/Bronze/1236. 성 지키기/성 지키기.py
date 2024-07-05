import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []

for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

a, b = 0, 0

for i in range(n):
    if "X" not in arr[i]:
        a += 1

for j in range(m):
    if "X" not in [arr[i][j] for i in range(n)]:
        b += 1

print(max(a, b))
