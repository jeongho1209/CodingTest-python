import sys

N = int(sys.stdin.readline().rstrip())

arr = []

ans = 0

for _ in range(N):
    time, money = map(int, sys.stdin.readline().rstrip().split())

    arr.append((time, money))


def dfs(idx, t, m):
    global ans
    if t > N:
        return

    if idx > N:
        return

    if idx == N:
        if ans < m:
            ans = m
        return

    dfs(idx + arr[idx][0], t + arr[idx][0], m + arr[idx][1])
    dfs(idx + 1, t, m)


dfs(0, 0, 0)

print(ans)
