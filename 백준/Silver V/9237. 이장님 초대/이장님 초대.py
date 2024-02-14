import sys

n = int(sys.stdin.readline().rstrip())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

trees.sort(reverse=True)

ans = []

for i in range(n):
    ans.append(1 + trees[i] + i)

print(max(ans) + 1)
