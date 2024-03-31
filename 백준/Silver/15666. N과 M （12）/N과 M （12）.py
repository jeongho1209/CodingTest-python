import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

ans = []


def dfs(idx):
    if len(ans) == M:
        print(*ans)
        return

    current = 0
    for i in range(idx, N):
        if current != arr[i]:
            current = arr[i]
            ans.append(arr[i])
            dfs(i)
            ans.pop()


dfs(0)
