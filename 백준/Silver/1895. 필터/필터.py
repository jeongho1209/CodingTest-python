import sys

R, C = map(int, sys.stdin.readline().rstrip().split())

pixels = []

for _ in range(R):
    pixels.append(list(map(int, sys.stdin.readline().rstrip().split())))

target = int(sys.stdin.readline().rstrip())

answer = []

for r in range(R - 2):
    for c in range(C - 2):
        targets = []
        for f1 in range(3):
            for f2 in range(3):
                targets.append(pixels[f1 + r][f2 + c])
        targets.sort()
        answer.append(targets[4])

ans = 0

for a in answer:
    if a >= target:
        ans += 1

print(ans)