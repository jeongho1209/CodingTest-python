import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque()

while True:
    packet = int(sys.stdin.readline().rstrip())

    if packet == -1:
        break

    if packet == 0:
        queue.popleft()
    elif len(queue) < N:
        queue.append(packet)

if not queue:
    print('empty')
else:
    print(*queue)
