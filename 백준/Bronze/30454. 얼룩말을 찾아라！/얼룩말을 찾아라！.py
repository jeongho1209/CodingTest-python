import sys

N, L = map(int, sys.stdin.readline().rstrip().split())

arrs = []

cnts = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    arrs.append(arr)
    ans = 0

    if arr[-1] == 1:
        ans += 1

    for i in range(len(arr) - 1):
        if arr[i] == 1:
            if arr[i + 1] == 1:
                continue
            else:
                ans += 1

    cnts.append(ans)

value_ans = max(cnts)
cnt_ans = 0

for arr in arrs:
    ans = 0

    if arr[-1] == 1:
        ans += 1

    for i in range(len(arr) - 1):
        if arr[i] == 1:
            if arr[i + 1] == 1:
                continue
            else:
                ans += 1

    if ans == value_ans:
        cnt_ans += 1

print(value_ans, cnt_ans)
