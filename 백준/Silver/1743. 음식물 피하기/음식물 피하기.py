import sys

sys.setrecursionlimit(10 ** 7)

height, width, k = map(int, sys.stdin.readline().rstrip().split())

graph = [['.'] * width for _ in range(height)]

visited = [[False] * width for _ in range(height)]

ans = 0

answers = []

for _ in range(k):
    r, c = map(int, sys.stdin.readline().rstrip().split())

    graph[r - 1][c - 1] = '#'


def dfs(h, w):
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]

    for i in range(4):
        dx = h + nx[i]
        dy = w + ny[i]

        if 0 <= dx < height and 0 <= dy < width:
            if not visited[dx][dy] and graph[dx][dy] == '#':
                visited[dx][dy] = True
                global ans
                ans += 1
                dfs(dx, dy)


for i in range(height):
    for j in range(width):
        if not visited[i][j] and graph[i][j] == '#':
            dfs(i, j)
            answers.append(ans)
        ans = 0

print(max(answers))
