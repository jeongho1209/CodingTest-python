import sys

sys.setrecursionlimit(10 ** 7)


def dfs(t):
    for i in graph[t]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


node, edge = map(int, sys.stdin.readline().rstrip().split())

graph = [[] * (node + 1) for _ in range(node + 1)]
visited = [False] * (node + 1)
cnt = 0

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().rstrip().split())
    graph[src].append(dest)
    graph[dest].append(src)

for i in range(1, node + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
