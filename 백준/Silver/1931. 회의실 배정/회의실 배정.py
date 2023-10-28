import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

arr.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_time = 0

for start, end in arr:
    if start >= end_time:
        answer += 1
        end_time = end

print(answer)