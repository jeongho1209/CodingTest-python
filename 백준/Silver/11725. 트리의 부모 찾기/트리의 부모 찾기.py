import sys

sys.setrecursionlimit(10 ** 7)


def dfs(pn):
    for t in trees[pn]:
        if not visited[t]:
            visited[t] = True
            answer[t] = pn
            dfs(t)


node = int(sys.stdin.readline().rstrip())

visited = [0] * (node + 1)
trees = [[] for _ in range(node + 1)]

answer = [0] * (node + 2)

for _ in range(node - 1):
    src, dest = map(int, sys.stdin.readline().rstrip().split())
    trees[src].append(dest)
    trees[dest].append(src)

dfs(1)

for i in range(2, node + 1):
    print(answer[i])
