import sys

sys.setrecursionlimit(10 ** 7)


def dfs(s):
    if visited[s]:
        return 0

    visited[s] = True

    if s + stone[s] < n:
        dfs(s + stone[s])
    if 0 <= s - stone[s] < s:
        dfs(s - stone[s])


n = int(sys.stdin.readline().rstrip())

stone = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [False] * n

start = int(sys.stdin.readline().rstrip())

dfs(start - 1)

result = 0
for i in visited:
    if i:
        result += 1

print(result)
