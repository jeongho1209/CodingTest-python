import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()
for i in range(n):
    num = list(map(int, sys.stdin.readline().strip().split()))
    len_q = len(queue)
    if num[0] == 1:
        queue.appendleft(num[1])
    elif num[0] == 2:
        queue.append(num[1])
    elif num[0] == 3:
        print(queue.popleft() if len_q else -1)
    elif num[0] == 4:
        print(queue.pop() if len_q else -1)
    elif num[0] == 5:
        print(len(queue))
    elif num[0] == 6:
        print(0 if len_q else 1)
    elif num[0] == 7:
        print(queue[0] if len_q else -1)
    elif num[0] == 8:
        print(queue[-1] if len_q else -1)
