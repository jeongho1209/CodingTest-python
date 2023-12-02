import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

answer = 0

pictures = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    # (1, 1), (1, 2), (2, 1), (2, 2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            pictures[i - 1][j - 1] += 1

for picture in pictures:
    for target in picture:
        if target > M:
            answer += 1

print(answer)
