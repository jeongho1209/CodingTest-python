import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()

ans = []


def dfs():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in nums:
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()


dfs()
