import sys

N = int(sys.stdin.readline().rstrip())

arr = [i for i in range(1, N)]

print(N, end=" ")
print(*arr)
