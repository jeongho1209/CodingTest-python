import sys

N = int(sys.stdin.readline().rstrip())

trees = [[] for i in range(N + 1)]

cnts = [0 for _ in range(N + 1)]

root = 1

for i in range(1, N + 1):
    parent_tree = int(sys.stdin.readline().rstrip())

    if parent_tree == -1:
        root = i
        continue
    trees[parent_tree].append(i)


def dfs(num, cnt):
    for i in range(len(trees[num])):
        next = trees[num][i]
        cnts[next] = cnt + 1
        dfs(next, cnt + 1)


dfs(root, 0)

for i in cnts[1:]:
    print(i)
