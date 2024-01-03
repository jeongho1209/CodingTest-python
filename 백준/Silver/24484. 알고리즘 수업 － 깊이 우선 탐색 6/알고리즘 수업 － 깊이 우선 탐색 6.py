import sys

sys.setrecursionlimit(10 ** 7)
node, edge, R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(node + 1)]
visited1 = [-1] * (node + 1)
visited2 = [0] * (node + 1)
cnt = 1

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().rstrip().split())

    graph[src].append(dest)
    graph[dest].append(src)


def dfs(t, depth):
    global cnt
    visited1[t] = depth
    visited2[t] = cnt
    graph[t].sort(reverse=True)

    for i in graph[t]:
        if visited1[i] == -1 and visited2[i] == 0:
            cnt += 1
            dfs(i, depth + 1)


dfs(R, 0)

answer = 0

for v1, v2 in zip(visited1[1:], visited2[1:]):
    answer += v1 * v2

print(answer)
