import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

arr = [i for i in range(1, N + 1)]

queue = deque(arr)

ans = []

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, ans)), end='')
print('>')
