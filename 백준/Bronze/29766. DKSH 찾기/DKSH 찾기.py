import sys

target = sys.stdin.readline().rstrip()

target = target.replace('DKSH', '1')

ans = 0

for t in target:
    if t == '1':
        ans += 1

print(ans)