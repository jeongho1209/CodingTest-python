import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

if A + B == C:
    print('correct!')
else:
    print('wrong!')