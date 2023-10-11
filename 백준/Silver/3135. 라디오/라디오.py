import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

result = abs(A - B)

for _ in range(int(sys.stdin.readline().rstrip())):
    K = int(sys.stdin.readline().rstrip())
    if result > abs(K - B):
        result = abs(K - B) + 1

print(result)