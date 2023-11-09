import sys

sys.setrecursionlimit(10 ** 7)

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = []

answer = 0

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))


def dfs(i, j):
    if N <= i or M <= j or i < 0 or j < 0 or graph[i][j] == 'X':
        return 0

    global answer

    if graph[i][j] == 'P':
        answer += 1

    if graph[i][j] != 'X':
        graph[i][j] = 'X'
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            dfs(i, j)

if answer == 0:
    print('TT')
else:
    print(answer)
