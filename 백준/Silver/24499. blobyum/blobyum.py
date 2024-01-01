import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

pies = list(map(int, sys.stdin.readline().rstrip().split()))

window = sum(pies[:k])

answer = window

for i in range(k, n + k):
    ni = i % n  # 원형이기 때문에 넘어갔을 때 처리
    window += pies[ni] - pies[ni - k]
    answer = max(answer, window)

print(answer)
