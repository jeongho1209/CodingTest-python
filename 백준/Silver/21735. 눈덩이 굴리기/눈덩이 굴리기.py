import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

ans = -1


def dfs(idx, value, time):
    global ans

    if time > M:
        return

    if time <= M:
        ans = max(ans, value)

    if idx <= N - 1:
        dfs(idx + 1, value + arr[idx + 1], time + 1)

    if idx <= N - 2:
        dfs(idx + 2, value // 2 + arr[idx + 2], time + 1)


dfs(0, 1, 0)

print(ans)
