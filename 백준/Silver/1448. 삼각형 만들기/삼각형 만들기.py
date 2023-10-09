import sys

# 시간 복잡도 안 되면 최소 힙 사용

n = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)
answer = []

for i in range(1, len(arr) - 1):
    if arr[i - 1] < arr[i] + arr[i + 1]:
        answer.append(arr[i - 1] + arr[i] + arr[i + 1])

if answer:
    print(max(answer))
else:
    print(-1)
