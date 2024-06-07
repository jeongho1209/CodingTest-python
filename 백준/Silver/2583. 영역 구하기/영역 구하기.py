import sys
sys.setrecursionlimit(10 ** 7)

height, width, k = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * width for _ in range(height)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

cnt = 0
ans_cnt = 0
answer = []


def dfs(h, w):
    global cnt

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for index in range(4):
        nx = dx[index] + h
        ny = dy[index] + w

        if 0 <= nx < height and 0 <= ny < width:
            if graph[nx][ny] == 0:
                cnt += 1
                graph[nx][ny] = 1
                dfs(nx, ny)


for i in range(height):
    for j in range(width):
        if graph[i][j] == 0:
            dfs(i, j)
            ans_cnt += 1

            if cnt == 0:
                cnt += 1
            answer.append(cnt)
            cnt = 0

print(ans_cnt)
print(*sorted(answer))
