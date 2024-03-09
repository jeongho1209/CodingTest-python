import sys

fn = list(map(int, sys.stdin.readline().rstrip().split()))

c = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

answer = 0

if fn[0] * n + fn[1] <= c * n and fn[0] <= c:
    answer = 1

print(answer)
