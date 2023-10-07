import sys

_ = sys.stdin.readline().rstrip()

arr = list(map(int, sys.stdin.readline().rstrip().split()))

mid = 0

lenArr = len(arr)

if lenArr % 2 == 0:
    mid = lenArr // 2 - 1
else:
    mid = lenArr // 2

arr.sort()

print(arr[mid])
