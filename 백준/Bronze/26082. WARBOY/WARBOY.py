import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

target = B / A

print(int(target * 3 * C))
