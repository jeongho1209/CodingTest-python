from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

queue = deque([(n, 0)])
real_time, cnt = 10 ** 6, 0

while queue:
    current, time = queue.popleft()
    visited[current] = True
    if current == k and time <= real_time:
        real_time = min(real_time, time)
        cnt += 1
    if time > real_time:
        break

    for x in (current - 1, current + 1, current * 2):
        if x in range(100001) and not visited[x]:
            queue.append((x, time + 1))

print(real_time)
print(cnt)
