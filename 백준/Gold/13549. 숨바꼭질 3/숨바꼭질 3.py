import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

visited = [False] * 100001
q = deque([(n, 0)])

while q:
    cur, time = q.popleft()
    visited[cur] = True

    if cur == k:
        print(time)
        exit()

    for i in (cur + 1, cur - 1, cur * 2):
        if i in range(100001) and not visited[i]:
            if i == cur * 2:
                q.appendleft((i, time))
            else:
                q.append((i, time + 1))
