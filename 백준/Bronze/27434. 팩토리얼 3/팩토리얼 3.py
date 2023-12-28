import sys

N = int(sys.stdin.readline().rstrip())

answer = 1

for i in range(1, N + 1):
    answer *= i

print(answer)
