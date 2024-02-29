import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    A, B, X = map(int, sys.stdin.readline().rstrip().split())

    print(A * (X - 1) + B)
