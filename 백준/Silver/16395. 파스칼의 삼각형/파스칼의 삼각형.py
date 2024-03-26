import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = [[1 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

print(arr[n - 1][k - 1])
