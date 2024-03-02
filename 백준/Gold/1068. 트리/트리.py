import sys

sys.setrecursionlimit(10 ** 7)


def dfs(num):
    trees[num] = -2
    for i in range(len(trees)):
        if num == trees[i]:
            dfs(i)


N = int(sys.stdin.readline().rstrip())

trees = list(map(int, sys.stdin.readline().rstrip().split()))

del_target = int(sys.stdin.readline().rstrip())

cnt = 0

dfs(del_target)

for i in range(len(trees)):
    if trees[i] != -2 and i not in trees:
        cnt += 1

print(cnt)
