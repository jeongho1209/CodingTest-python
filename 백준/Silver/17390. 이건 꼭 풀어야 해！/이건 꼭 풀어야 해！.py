import sys

_, q = map(int, sys.stdin.readline().rstrip().split())

arr = [0]

arr += list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

for _ in range(q):
    L, R = map(int, sys.stdin.readline().rstrip().split())
    print(arr[R] - arr[L - 1])
