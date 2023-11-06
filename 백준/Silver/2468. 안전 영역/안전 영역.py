import sys

sys.setrecursionlimit(10 ** 7)

n = int(sys.stdin.readline().rstrip())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

max_graph_value = max(map(max, graph))

answer = 1


def dfs(i, j, k):
    if i >= n or j >= n or i < 0 or j < 0:
        return 0

    if not visited[i][j] and graph[i][j] > k:
        visited[i][j] = True
        dfs(i + 1, j, k)
        dfs(i, j + 1, k)
        dfs(i - 1, j, k)
        dfs(i, j - 1, k)


for k in range(max_graph_value):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                cnt += 1
                dfs(i, j, k)
    answer = max(answer, cnt)

print(answer)
