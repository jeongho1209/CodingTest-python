import sys

N, L = map(int, sys.stdin.readline().rstrip().split())

for _ in range(L - 1):
    print(1, end="")

print(N)
