import sys

ans = []


def dfs(depth, idx):
    if depth == 6:
        print(*ans)
        return

    for i in range(idx, k):
        if new_arr[i] not in ans:
            ans.append(new_arr[i])
            dfs(depth + 1, i + 1)
            ans.pop()


while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    k = arr[0]
    new_arr = arr[1:]
    dfs(0, 0)

    if k == 0:
        exit()

    print()
