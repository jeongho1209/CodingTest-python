import sys

_ = sys.stdin.readline().rstrip()

A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

ans += len(set(A) - set(B))
ans += len(set(B) - set(A))

print(ans)
