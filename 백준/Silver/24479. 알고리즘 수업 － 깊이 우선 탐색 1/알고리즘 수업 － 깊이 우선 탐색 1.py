import sys
sys.setrecursionlimit(10 ** 7)

cnt = 1


def dfs(target):
    global cnt
    visited[target] = cnt
    graph[target].sort()
    for i in graph[target]:
        if not visited[i]:
            cnt += 1
            dfs(i)


N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

for _ in range(M):
    U, V = map(int, sys.stdin.readline().rstrip().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
