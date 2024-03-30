import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

ans = []

visited_idx = []


def dfs():
    if len(ans) == M:
        print(*ans)
        return

    current = 0
    for i in range(N):
        if i not in visited_idx and current != arr[i]:
            current = arr[i]
            ans.append(arr[i])
            visited_idx.append(i)
            dfs()
            ans.pop()
            visited_idx.pop()


dfs()
