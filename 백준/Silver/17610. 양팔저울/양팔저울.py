import sys

K = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr_sum = sum(arr)

ans = set()

cnt = 0


def dfs(idx, value):
    if idx > K:
        return

    if idx == K:
        if value <= arr_sum:
            ans.add(value)
        return

    dfs(idx + 1, value + arr[idx])
    dfs(idx + 1, value)
    dfs(idx + 1, value - arr[idx])


dfs(0, 0)

for i in ans:
    if 0 <= i <= arr_sum:
        cnt += 1

print(arr_sum - cnt + 1)
