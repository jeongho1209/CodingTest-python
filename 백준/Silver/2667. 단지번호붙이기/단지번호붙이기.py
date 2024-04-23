import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = []

ans = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([(x, y)])
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1

    if cnt == 1:
        return cnt
    else:
        return cnt - 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))

for i in range(len(ans)):
    print(ans[i])
