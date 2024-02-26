import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    print(arr[b] - arr[a - 1])
