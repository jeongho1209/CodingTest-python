import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()

ans = []


def dfs(s):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(s, len(nums)):
        ans.append(nums[i])
        dfs(i)
        ans.pop()


dfs(0)
