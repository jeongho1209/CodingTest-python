import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())

    scores = []

    for _ in range(M):
        scores.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = {}

    for i in range(N):
        target = 1
        for j in range(M):
            target *= scores[j][i]
        result[target] = i + 1

    print(result[max(result)])
