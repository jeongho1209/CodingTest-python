import sys

N, target = map(int, sys.stdin.readline().rstrip().split())

medal = []

for _ in range(N):
    medal.append(list(map(int, sys.stdin.readline().rstrip().split())))

medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [medal[i][0] for i in range(N)].index(target)

for i in range(N):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break
