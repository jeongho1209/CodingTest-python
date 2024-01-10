import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [] * N

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0)])

visited = {(0, 0)}

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if (nx, ny) not in visited and graph[nx][ny]:
                visited.add((nx, ny))
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

print(graph[-1][-1])
