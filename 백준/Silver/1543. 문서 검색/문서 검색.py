import sys

targets = sys.stdin.readline().rstrip()
n = sys.stdin.readline().rstrip()

cnt = 0

for i in range(len(targets)):
    target = targets[i:len(n) + i]
    if target == n:
        targets = targets.replace(target, '3')

for target in targets:
    if target == '3':
        cnt += 1

print(cnt)