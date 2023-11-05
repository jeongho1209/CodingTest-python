import sys

sys.setrecursionlimit(10 ** 7)


def dfs(i, j, N, M):
    if i >= M or j >= N or i < 0 or j < 0:
        return 0
    if graph[i][j] == 1:
        graph[i][j] = 0
        dfs(i + 1, j, N, M)
        dfs(i, j + 1, N, M)
        dfs(i - 1, j, N, M)
        dfs(i, j - 1, N, M)


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cnt = 0
    M, N, K = map(int, sys.stdin.readline().rstrip().split())

    graph = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        graph[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] != 0:  # 0이 아닐때만 카운트
                dfs(i, j, N, M)
                cnt += 1

    print(cnt)
