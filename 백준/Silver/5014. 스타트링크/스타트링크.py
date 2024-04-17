import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split())

queue = deque([(S, 0)])

visited = [False] * 1000001

ans = -1

while queue:
    current, cnt = queue.popleft()

    if current == G:
        ans = cnt
        break

    if visited[current]:
        continue

    visited[current] = True

    if current + U <= F:
        queue.append((current + U, cnt + 1))
    if current - D >= 1:
        queue.append((current - D, cnt + 1))

if ans == -1:
    print('use the stairs')
    exit()

print(ans)
