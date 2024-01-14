import sys

n = int(sys.stdin.readline().rstrip())

sticks = []

ans = 1

for _ in range(n):
    sticks.append(int(sys.stdin.readline().rstrip()))

sticks.reverse()

target = sticks[0]

for i in range(1, n):
    if target < sticks[i]:
        target = sticks[i]
        ans += 1

print(ans)
