import sys

n = int(sys.stdin.readline().rstrip())

files = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

cluster = int(sys.stdin.readline().rstrip())

for f in files:
    if f % cluster > 0:
        ans += f // cluster + 1
    else:
        ans += f // cluster

print(ans * cluster)
