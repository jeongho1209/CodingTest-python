import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
arr = [False] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if not arr[j]:
            arr[j] = True
            cnt += 1
            if cnt == K:
                print(j)
