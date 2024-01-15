import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

words = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        continue

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for k, v in sorted_words:
    print(k)
