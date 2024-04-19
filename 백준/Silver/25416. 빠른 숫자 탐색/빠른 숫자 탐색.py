import sys
from collections import deque

graph = []

for _ in range(5):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[False] * 5 for _ in range(5)]

r, c = map(int, sys.stdin.readline().rstrip().split())

ans = -1

queue = deque([(r, c, 0)])

while queue:
    x, y, cnt = queue.popleft()

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if graph[x][y] == 1:
        ans = cnt
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny] and graph[nx][ny] != -1:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

print(ans)
