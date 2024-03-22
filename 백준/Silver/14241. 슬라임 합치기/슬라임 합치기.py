import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort(reverse=True)

ans = 0

for i in range(N - 1):
    score = arr[i + 1] * arr[i]
    arr[i + 1] += arr[i]
    ans += score

print(ans)
