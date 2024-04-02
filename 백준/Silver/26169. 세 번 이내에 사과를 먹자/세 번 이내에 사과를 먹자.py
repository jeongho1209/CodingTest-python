import sys

arr = []

visited = [[False] * 5 for _ in range(5)]

for _ in range(5):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

r, c = map(int, sys.stdin.readline().rstrip().split())


def dfs(x, y, depth, cnt):
    visited[x][y] = True

    if arr[x][y] == 1:
        cnt += 1

    if cnt >= 2:
        return 1

    if depth > 2:
        visited[x][y] = False
        return

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny] and arr[nx][ny] != -1:
                if dfs(nx, ny, depth + 1, cnt) == 1:
                    return 1

    visited[x][y] = False
    return 0


print(dfs(r, c, 0, 0))
