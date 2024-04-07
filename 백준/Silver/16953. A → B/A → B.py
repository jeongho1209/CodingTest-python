import sys
from collections import deque

A, target = map(int, sys.stdin.readline().rstrip().split())

queue = deque([(A, 1)])

while queue:
    current, cnt = queue.popleft()

    if current > target:
        continue

    if current == target:
        print(cnt)
        exit()

    queue.append((int(str(current) + '1'), cnt + 1))
    queue.append((current * 2, cnt + 1))

print(-1)
