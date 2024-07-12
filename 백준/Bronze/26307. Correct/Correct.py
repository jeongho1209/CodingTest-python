import sys

h, m = map(int, sys.stdin.readline().rstrip().split())

start = 540

s = h * 60 + m

gap = abs(s - start)

print(gap)
