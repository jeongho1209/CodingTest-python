import sys

_ = sys.stdin.readline()
scores = list(map(int, sys.stdin.readline().rstrip().split()))

SUM = 0
ans = 0

for i in range(len(scores)):
    if scores[i] == 1:
        SUM += 1
        ans += SUM
    else:
        SUM = 0

print(ans)
