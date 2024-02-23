import sys

N = int(sys.stdin.readline().rstrip())

ans = 0

for _ in range(N):
    ans += int(sys.stdin.readline().rstrip())

print(ans - (N - 1))
