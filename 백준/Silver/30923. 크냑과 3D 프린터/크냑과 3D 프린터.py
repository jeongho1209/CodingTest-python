import sys

n = int(sys.stdin.readline().rstrip())

targets = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

if n == 1:
    print(targets[0] * 4 + 2)
    exit()

# 밑과 위는 n * 2
# 옆면 -> 배열 값 * 2
# 또 다른 옆면 하나 -> 0, -1 인덱스 더하기
# 차 구하기 -> abs(targets[i] - targets[i - 1))

for i in range(len(targets) - 1):
    ans += targets[i] * 2
    ans += abs(targets[i] - targets[i + 1])

ans += n * 2
ans += targets[0] + targets[-1] * 3

print(ans)