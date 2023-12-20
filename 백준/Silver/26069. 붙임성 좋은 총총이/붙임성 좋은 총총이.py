import sys

n = int(sys.stdin.readline().rstrip())

targets = {'ChongChong'}

for _ in range(n):
    p1, p2 = sys.stdin.readline().rstrip().split()

    if p1 in targets:
        targets.add(p2)

    if p2 in targets:
        targets.add(p1)

print(len(targets))
