import sys

N, L = map(int, sys.stdin.readline().rstrip().split())

counts = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    cnt = 0

    if arr[-1] == 1:
        cnt += 1

    for i in range(len(arr) - 1):
        if arr[i] == 1:
            if arr[i + 1] == 1:
                continue
            else:
                cnt += 1

    counts.append(cnt)

max_cnt = max(counts)

print(max_cnt, counts.count(max_cnt))
