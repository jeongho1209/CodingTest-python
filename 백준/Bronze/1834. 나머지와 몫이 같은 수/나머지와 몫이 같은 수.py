import sys

N = int(sys.stdin.readline().rstrip())

ans = 0

for i in range(1, N):
    ans += N * i + i

print(ans)