import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

visited = [False] * N


def dfs(idx, strength):
    global cnt

    if strength < 500:
        return

    if idx == N:
        cnt += 1
        return

    strength -= K

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(idx + 1, strength + arr[i])
            visited[i] = False


dfs(0, 500)

print(cnt)
