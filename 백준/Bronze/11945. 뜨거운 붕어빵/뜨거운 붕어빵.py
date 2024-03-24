import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

for _ in range(N):
    target = list(sys.stdin.readline().rstrip())[::-1]
    for i in target:
        print(i, end='')

    print()
