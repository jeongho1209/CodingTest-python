import sys

arr = list(map(int, sys.stdin.readline().rstrip().split()))

x, y, r = map(int, sys.stdin.readline().rstrip().split())

if x in arr:
    print(arr.index(x) + 1)
else:
    print(0)
   