import sys

N = int(sys.stdin.readline().rstrip())
targets = list(sys.stdin.readline().rstrip())

ans = 0

for t in targets:
    ans += ord(t) - 64

print(ans)
