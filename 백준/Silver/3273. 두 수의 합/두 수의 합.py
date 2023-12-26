import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

target = int(sys.stdin.readline().rstrip())

numbers.sort()

cnt = 0

start, end = 0, n - 1

while start < end:
    part_sum = numbers[start] + numbers[end]

    if part_sum < target:
        start += 1
    elif part_sum > target:
        end -= 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)