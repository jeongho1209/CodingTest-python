import sys

_, M = map(int, sys.stdin.readline().rstrip().split())

arr = []

for _ in range(M):
    arr.append(list(sys.stdin.readline().rstrip().split()))

arr.sort(key=lambda x: (int(x[1]), int(x[0])))

answer = ''

for i in arr:
    answer += i[2]

print(answer)