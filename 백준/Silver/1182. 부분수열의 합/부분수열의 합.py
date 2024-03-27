import sys

N, S = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

ans = []


def dfs(idx, value):
    global cnt

    if idx == N:
        if value == S:
            cnt += 1
        return
    else:
        dfs(idx + 1, value + arr[idx])
        dfs(idx + 1, value)


dfs(0, 0)

if S == 0:
    print(cnt - 1)
else:
    print(cnt)
