import sys

N = int(sys.stdin.readline().rstrip())

wait_queue = []

for _ in range(N):
    wait_queue.append(int(sys.stdin.readline().rstrip()))

# 고려할 것 -> 우선 내림차순 정렬해서 가장 많이 받을 수 있게 하는데 음수 안 나오게 하는것도 고려해야함

wait_queue.sort(reverse=True)

ans = 0

for k, v in enumerate(wait_queue):
    x = v - k
    if x > 0:
        ans += x

print(ans)
