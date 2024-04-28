import sys

target = sys.stdin.readline().rstrip()

ans = 0

for t in target:
    ans += int(t) ** 5

print(ans)
