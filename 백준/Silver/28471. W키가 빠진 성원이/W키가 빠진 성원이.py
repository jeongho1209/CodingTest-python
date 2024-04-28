import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [0, -1, 1, 0, 1, -1, -1]
dy = [-1, -1, -1, 1, 1, 0, 1]

cnt = 0


def bfs(i, j):
    global cnt
    queue = deque([(i, j)])
    visited = [[False] * N for _ in range(N)]
    while queue:
        x, y = queue.popleft()

        for k in range(7):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == '.':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == 'F':
            bfs(i, j)

print(cnt)
