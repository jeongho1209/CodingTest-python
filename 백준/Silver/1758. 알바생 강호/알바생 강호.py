import sys

N = int(sys.stdin.readline().rstrip())

wait_queue = []

for _ in range(N):
    wait_queue.append(int(sys.stdin.readline().rstrip()))

wait_queue.sort(reverse=True)

ans = 0

for k, v in enumerate(wait_queue):
    x = v - k
    if x > 0:
        ans += x

print(ans)
