import sys

n = int(sys.stdin.readline().rstrip())

arr = [1, 2]

for i in range(2, n):
    arr.append((arr[i - 1] + arr[i - 2]) % 10007)

print(arr[n - 1])
