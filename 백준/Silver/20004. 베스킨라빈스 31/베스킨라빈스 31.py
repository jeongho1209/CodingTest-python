import sys

A = int(sys.stdin.readline().rstrip())

for i in range(1, A + 1):
    if 30 % (i + 1) == 0:
        print(i)
