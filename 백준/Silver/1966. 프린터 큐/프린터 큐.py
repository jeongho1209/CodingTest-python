import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    print_queue = deque(list(map(int, sys.stdin.readline().split())))
    idx_queue = deque(list(range(N)))
    cnt = 0

    while print_queue:
        if print_queue[0] == max(print_queue):
            cnt += 1
            print_queue.popleft()
            if idx_queue.popleft() == M:
                print(cnt)
        else:
            print_queue.append(print_queue.popleft())
            idx_queue.append(idx_queue.popleft())