import sys
from collections import deque

A, K = map(int, sys.stdin.readline().rstrip().split())

queue = deque([(A, 0)])

set1 = set()

while queue:
    v, c = queue.popleft()
    if v == K:
        print(c)
        break

    if v * 2 <= K and v * 2 not in set1:
        set1.add(v * 2)
        queue.append([v * 2, c + 1])

    if v + 1 <= K and v + 1 not in set1:
        set1.add(v + 1)
        queue.append([v + 1, c + 1])
