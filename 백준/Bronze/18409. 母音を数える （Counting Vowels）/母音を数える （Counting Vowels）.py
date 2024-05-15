import sys

_ = sys.stdin.readline()
target = sys.stdin.readline().rstrip()

arr = ['a', 'e', 'i', 'o', 'u']

ans = 0

for t in target:
    if t in arr:
        ans += 1

print(ans)
