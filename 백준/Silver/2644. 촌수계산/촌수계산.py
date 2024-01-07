import sys

sys.setrecursionlimit(10 ** 7)

ans = 0


def dfs(target, cnt):
    global ans
    for t in graph[target]:
        if not visited[t]:
            visited[t] = True
            dfs(t, cnt + 1)
        if t == t2:
            ans = cnt
            return


n = int(sys.stdin.readline().rstrip())

t1, t2 = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

edge = int(sys.stdin.readline().rstrip())

for _ in range(edge):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(t1, 1)

if ans == 0:
    print(-1)
else:
    print(ans)
