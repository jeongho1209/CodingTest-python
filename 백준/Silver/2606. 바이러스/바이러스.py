import sys

node = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())
graph = [[0] * 101 for _ in range(101)]
dfsVis = [0] * 101
answer = 0

for _ in range(edge):
    i, j = map(int, sys.stdin.readline().split())
    graph[i][j] = 1
    graph[j][i] = 1


def dfs(q):
    global answer
    answer += 1
    dfsVis[q] = 1
    for k in range(1, node + 1):
        if graph[q][k] and not dfsVis[k]:
            dfs(k)


dfs(1)
print(answer - 1)
