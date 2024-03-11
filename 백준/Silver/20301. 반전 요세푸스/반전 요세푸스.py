import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().rstrip().split())

arr = [i for i in range(1, N + 1)]

cnt = 0

queue = deque(arr)

ans = []

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

    cnt += 1

    if cnt == M:
        queue.reverse()
        cnt = 0

for i in ans:
    print(i)
