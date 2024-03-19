import sys

sys.setrecursionlimit(10 ** 7)

R, C, K = map(int, sys.stdin.readline().rstrip().split())

home_map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, cnt):
    global ans
    if i == 0 and j == C - 1 and cnt == K:
        ans += 1

    for w in range(4):
        x = i + dx[w]
        y = j + dy[w]

        if 0 <= x < R and 0 <= y < C and home_map[x][y] != 'T':
            home_map[x][y] = 'T'
            dfs(x, y, cnt + 1)
            home_map[x][y] = '.'


home_map[R - 1][0] = 'T'
dfs(R - 1, 0, 1)

print(ans)
