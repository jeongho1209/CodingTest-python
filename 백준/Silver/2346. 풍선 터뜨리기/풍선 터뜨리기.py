import sys
from collections import deque

_ = sys.stdin.readline()
queue = deque(enumerate(map(int, sys.stdin.readline().rstrip().split())))

ans = []

while queue:
    idx, value = queue.popleft()

    if value > 0:
        queue.rotate(-(value - 1))
    else:
        queue.rotate(-value)

    ans.append(idx + 1)

print(*ans)
