import sys, math

x, y = map(int, sys.stdin.readline().rstrip().split())

print(math.trunc(x + y + min(x, y) // 10))