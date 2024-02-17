import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

roads = []

for _ in range(N):
    roads.append(list(map(int, sys.stdin.readline().rstrip().split())))

ans = []

for i in range(N):
    for j in range(M):
        if roads[i][j] == 1:
            ans.append((i, j))

x1, y1 = ans[0]
x2, y2 = ans[1]

print(abs(x2 - x1) + abs(y2 - y1))
