import sys

N = int(sys.stdin.readline().rstrip())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

answer = 0

for k, v in enumerate(arr):
    answer += abs(k + 1 - v)

print(answer)
