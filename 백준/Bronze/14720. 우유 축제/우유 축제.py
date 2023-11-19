import sys

_ = sys.stdin.readline().rstrip()
milk = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for i in range(len(milk)):
    if milk[i] == ans % 3:
        ans += 1

print(ans)