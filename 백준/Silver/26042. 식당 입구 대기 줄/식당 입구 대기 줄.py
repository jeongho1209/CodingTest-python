import sys

n = int(sys.stdin.readline().rstrip())

queue = []

ans = []

for _ in range(n):
    command = list(map(int, sys.stdin.readline().rstrip().split()))

    if command[0] == 1:
        queue.append(command[1])
        ans.append((len(queue), queue[-1]))
    else:
        queue.pop()

ans.sort(key=lambda x: (-x[0], x[1]))

print(*ans[0])
