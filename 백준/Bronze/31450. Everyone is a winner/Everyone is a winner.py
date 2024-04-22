import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

if N % M == 0:
    print('Yes')
else:
    print('No')
   