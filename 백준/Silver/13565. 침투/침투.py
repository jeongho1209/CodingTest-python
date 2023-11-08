import sys

sys.setrecursionlimit(10 ** 7)

M, N = map(int, sys.stdin.readline().rstrip().split())

graph = []

answer = 'NO'

visited = [[False] * N for _ in range(M)]

for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(i, j):
    if i >= M or i < 0 or j >= N or j < 0:
        return 0
    if not visited[i][j] and graph[i][j] == 0:
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)


for j in range(N):
    if not visited[0][j] and graph[0][j] != 1:
        dfs(0, j)

for i in range(N):
    if visited[M - 1][i]:
        answer = 'YES'

print(answer)
