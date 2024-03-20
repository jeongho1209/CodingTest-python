import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

ans = []


def dfs(k):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(k, N):
        if arr[i] not in ans:
            ans.append(arr[i])
            dfs(i + 1)
            ans.pop()


dfs(0)
