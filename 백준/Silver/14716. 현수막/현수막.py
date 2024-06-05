import sys

sys.setrecursionlimit(10 ** 7)

height, width = map(int, sys.stdin.readline().rstrip().split())

graph = []

cnt = 0

for _ in range(height):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[False] * width for _ in range(height)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]


def dfs(h, w):
    for index in range(8):
        nx = h + dx[index]
        ny = w + dy[index]

        if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(nx, ny)


for i in range(height):
    for j in range(width):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)
