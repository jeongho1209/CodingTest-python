import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque([i for i in range(1, N + 1)])

k = 1

while len(queue) != 1:
    for i in range((k ** 3 - 1) % len(queue)):
        queue.append(queue.popleft())
    queue.popleft()
    k += 1

print(queue[0])
