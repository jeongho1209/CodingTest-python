import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    L = int(sys.stdin.readline().rstrip())

    cx, cy = map(int, sys.stdin.readline().rstrip().split())

    tx, ty = map(int, sys.stdin.readline().rstrip().split())

    queue = deque([(cx, cy, 0)])

    visited = [[False] * L for _ in range(L)]

    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    while queue:
        x, y, cnt = queue.popleft()

        if x == tx and y == ty:
            print(cnt)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < L and 0 <= ny < L:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))
