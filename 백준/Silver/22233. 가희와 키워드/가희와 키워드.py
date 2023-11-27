import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

memo = {}

answer = []

for _ in range(N):
    key_word = sys.stdin.readline().rstrip()
    if key_word not in memo:
        memo[key_word] = 1

for _ in range(M):
    key_words = list(sys.stdin.readline().rstrip().split(','))

    for key in key_words:
        if key in memo:
            memo.pop(key)

    answer.append(len(memo))

for i in answer:
    print(i)