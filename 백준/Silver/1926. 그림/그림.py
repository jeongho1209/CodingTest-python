import sys
sys.setrecursionlimit(10 ** 7)

n, m = map(int, sys.stdin.readline().rstrip().split())  # 세로, 가로

graph = []

picture_count = 0
picture_area = 0
max_picture_area = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


def dfs(i, j):
    if i >= n or j >= m or i < 0 or j < 0:
        return 0

    if graph[i][j] == 1:
        global picture_area
        picture_area += 1
        graph[i][j] = 0
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            picture_count += 1
            max_picture_area.append(picture_area)
        picture_area = 0

if picture_count == 0:
    max_picture_area.append(0)

print(picture_count)
print(max(max_picture_area))
