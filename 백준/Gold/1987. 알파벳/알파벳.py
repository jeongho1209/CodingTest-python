import sys
sys.setrecursionlimit(10 ** 5)

height, width = map(int, sys.stdin.readline().rstrip().split())

graph = []

visited = [0] * 26

ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(height):
    graph.append(list(sys.stdin.readline().rstrip()))


def dfs(h, w, cnt):
    global ans

    if ans <= cnt:
        ans = cnt

    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]

        if 0 <= nx < height and 0 <= ny < width and not visited[ord(graph[nx][ny]) - 65]:
            visited[ord(graph[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt + 1)
            visited[ord(graph[nx][ny]) - 65] = 0


visited[ord(graph[0][0]) - 65] = 1
dfs(0, 0, 1)

print(ans)
