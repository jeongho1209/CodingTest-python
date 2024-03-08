import sys

_ = sys.stdin.readline()
print(*sorted(
    list(map(int, sys.stdin.readline().rstrip().split())) + list(map(int, sys.stdin.readline().rstrip().split()))))
