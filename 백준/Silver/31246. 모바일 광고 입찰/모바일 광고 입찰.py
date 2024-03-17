import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

ads = []

ans = 0

for _ in range(n):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    ads.append(B - A)

ads.sort()

if ads[k - 1] < 0:
    print(0)
    exit()
else:
    print(ads[k - 1])
