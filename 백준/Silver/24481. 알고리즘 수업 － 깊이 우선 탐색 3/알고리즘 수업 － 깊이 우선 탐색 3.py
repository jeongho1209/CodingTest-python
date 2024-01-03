import sys

sys.setrecursionlimit(10 ** 7)
node, edge, R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(node + 1)]
visited = [-1] * (node + 1)

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().rstrip().split())

    graph[src].append(dest)
    graph[dest].append(src)


def dfs(t, depth):
    visited[t] = depth
    graph[t].sort()

    for i in graph[t]:
        if visited[i] == -1:
            dfs(i, depth + 1)


dfs(R, 0)

for i in visited[1:]:
    print(i)
