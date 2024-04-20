import sys
from collections import deque

dx = (1, 0)
dy = (0, 1)

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

visited = [[False] * M for _ in range(N)]

ans = 'No'

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    if x == N - 1 and y == M - 1:
        ans = 'Yes'
        break

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 1:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

print(ans)
