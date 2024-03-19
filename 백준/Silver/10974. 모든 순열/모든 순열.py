import sys

N = int(sys.stdin.readline().rstrip())

ans = []


def dfs(k):
    if len(ans) == N:
        print(*ans)

    for i in range(1, N + 1):
        if i not in ans:
            ans.append(i)
            dfs(i)
            ans.pop()


dfs(1)
