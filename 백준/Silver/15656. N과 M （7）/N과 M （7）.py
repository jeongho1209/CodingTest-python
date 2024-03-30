import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

ans = []


def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        ans.append(arr[i])
        dfs()
        ans.pop()


dfs()
