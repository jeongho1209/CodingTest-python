import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

arr = []

for _ in range(K):
    arr.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2

    cnt = 0

    for i in arr:
        cnt += i // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
