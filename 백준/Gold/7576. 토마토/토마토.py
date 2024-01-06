import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())

graph = []

cnt = 0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

queue = deque()

for i in range(N):  # 세로
    for j in range(M):  # 가로
        if graph[i][j] == 1:
            queue.append([i, j])  # 세로 가로


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()  # 세로 가로

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])


bfs()

ans = 0

for g in graph:
    for k in g:
        if k == 0:
            print(-1)
            exit()
    ans = max(ans, max(g))

print(ans - 1)
