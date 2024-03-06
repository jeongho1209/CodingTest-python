import sys

N = int(sys.stdin.readline().rstrip())

ans = 0
stack = []

for _ in range(N):
    command = list(map(int, sys.stdin.readline().rstrip().split()))

    if command[0] == 1:
        stack.append((command[1], command[2]))

    if stack:
        score, time = stack.pop()
        time -= 1
        if time == 0:
            ans += score
        else:
            stack.append((score, time))

print(ans)
