import sys

sys.setrecursionlimit(10 ** 6)

t = int(sys.stdin.readline().rstrip())


def dfs(h, w):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for k in range(4):
        nx = h + dx[k]
        ny = w + dy[k]

        if 0 <= nx < height and 0 <= ny < width:
            if graph[nx][ny] == '#':
                graph[nx][ny] = '.'
                dfs(nx, ny)


for _ in range(t):
    height, width = map(int, sys.stdin.readline().rstrip().split())

    graph = []

    cnt = 0

    for _ in range(height):
        graph.append(list(sys.stdin.readline().rstrip()))

    for i in range(height):
        for j in range(width):
            if graph[i][j] == '#':
                dfs(i, j)
                cnt += 1

    print(cnt)
