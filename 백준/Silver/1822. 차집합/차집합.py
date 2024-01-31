import sys

_, _ = map(int, sys.stdin.readline().rstrip().split())

A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

target = sorted(list(set(A) - set(B)))

print(len(target))
print(' '.join(map(str, target)))
