import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

queue = deque([(N, 0)])

distinct_set = set()

while queue:
    v, cnt = queue.popleft()

    if v == K:
        print(cnt)
        break

    if v * 2 <= K + 1 and v * 2 not in distinct_set:
        distinct_set.add(v * 2)
        queue.append([v * 2, cnt + 1])

    if v + 1 <= K and v + 1 not in distinct_set:
        distinct_set.add(v + 1)
        queue.append([v + 1, cnt + 1])

    if v - 1 not in distinct_set:
        distinct_set.add(v - 1)
        queue.append([v - 1, cnt + 1])
