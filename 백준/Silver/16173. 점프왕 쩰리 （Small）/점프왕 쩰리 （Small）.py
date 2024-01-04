N = int(input())

graph = []
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))


def dfs(i, j):
    if i < 0 or j < 0 or i >= N or j >= N:
        return 0

    if not visited[i][j]:
        visited[i][j] = True
        dfs(i + graph[i][j], j)
        dfs(i, j + graph[i][j])


dfs(0, 0)

if visited[N - 1][N - 1]:
    print("HaruHaru")
else:
    print("Hing")
