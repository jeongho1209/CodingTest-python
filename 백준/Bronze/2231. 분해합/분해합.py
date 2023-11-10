import sys

N = int(sys.stdin.readline().rstrip())

answer = []

for i in range(1, N + 1):
    nums = list(map(int, str(i)))
    result = i + sum(nums)

    if result == N:
        answer.append(i)
if answer:
    print(min(answer))
else:
    print(0)