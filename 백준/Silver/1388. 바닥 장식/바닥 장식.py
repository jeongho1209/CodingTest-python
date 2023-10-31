import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []

cnt = 0


def dfs(q, w, t):
    if q >= n or w >= m or t != graph[q][w]:
        return 0
    if t == '-':
        graph[q][w] = 'A'
        dfs(q, w + 1, t)
        return 1
    elif t == '|':
        graph[q][w] = 'A'
        dfs(q + 1, w, t)
        return 1
    return 1


for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] != 'A':
            cnt += 1
            dfs(i, j, graph[i][j])

print(cnt)
