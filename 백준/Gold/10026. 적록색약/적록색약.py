import sys

sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline().rstrip())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = 0
blind_cnt = 0

visited = [[False] * N for _ in range(N)]


def dfs(i, j, t):
    if i >= N or j >= N or i < 0 or j < 0:
        return 0

    if graph[i][j] == t and not visited[i][j]:
        visited[i][j] = True
        dfs(i + 1, j, t)
        dfs(i, j + 1, t)
        dfs(i - 1, j, t)
        dfs(i, j - 1, t)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            blind_cnt += 1

print(cnt, blind_cnt)
