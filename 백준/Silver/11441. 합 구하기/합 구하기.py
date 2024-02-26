import sys

_ = sys.stdin.readline()

arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())

    print(arr[B] - arr[A - 1])
