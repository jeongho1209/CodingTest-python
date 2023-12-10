import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())

scores = {}

ans = 0

for _ in range(N):
    name, score = sys.stdin.readline().rstrip().split()
    scores[name] = int(score)

for _ in range(K):
    target = sys.stdin.readline().rstrip()
    ans += scores[target]
    del scores[target]

max_ans, min_ans = ans, ans

scores = sorted(scores.items(), key=lambda x: x[1])

for i in range(M - K):
    min_ans += scores[i][1]
    max_ans += scores[-i - 1][1]

print(min_ans, max_ans)
