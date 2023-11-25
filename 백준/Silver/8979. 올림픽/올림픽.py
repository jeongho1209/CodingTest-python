import sys

N, target = map(int, sys.stdin.readline().rstrip().split())

medal = []

for _ in range(N):
    medal.append(list(map(int, sys.stdin.readline().rstrip().split())))

medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

ans = 0

for k, v in enumerate(medal):
    if v[0] == target:
        ans = k
        break

print(ans)
