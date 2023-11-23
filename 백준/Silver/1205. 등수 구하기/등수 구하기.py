import sys

N, score, P = map(int, sys.stdin.readline().rstrip().split())

if N == 0:
    print(1)
    exit()

ranking = list(map(int, sys.stdin.readline().rstrip().split()))
ranking.append(score)
ranking.sort(reverse=True)
ans = ranking.index(score) + 1

if N == P and score <= ranking[-1]:  # 랭킹에 들 수 없다면
    ans = -1

print(ans)
