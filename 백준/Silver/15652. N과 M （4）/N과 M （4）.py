import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

ans = []


def dfs(s):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(s, N + 1):
        if i >= s:
            ans.append(i)
            dfs(i)
            ans.pop()


dfs(1)
