import sys

X, Y = map(int, sys.stdin.readline().rstrip().split())
Z = 100 * Y // X

if Z >= 99:
    print(-1)
    exit()

left = 0
right = X
res = X

while left <= right:
    mid = (left + right) // 2

    if 100 * (Y + mid) // (X + mid) > Z:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
