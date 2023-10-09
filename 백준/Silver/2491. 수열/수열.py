import sys

_ = sys.stdin.readline().rstrip()
arr = list(map(int, sys.stdin.readline().rstrip().split()))
upDp = [1] * 100000
downDp = [1] * 100000

for i in range(1, len(arr)):
    if arr[i] >= arr[i - 1]:
        upDp[i] = upDp[i - 1] + 1
    if arr[i] <= arr[i - 1]:
        downDp[i] = downDp[i - 1] + 1

upMax = max(upDp)
downMax = max(downDp)

print(max(upMax, downMax))
