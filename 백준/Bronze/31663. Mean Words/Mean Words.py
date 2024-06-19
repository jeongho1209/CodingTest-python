import sys

n = int(sys.stdin.readline().rstrip())

words = []

for _ in range(n):
    words.append(list(sys.stdin.readline().rstrip()))

max_len = max(len(word) for word in words)
sums = [0] * max_len
counts = [0] * max_len

for word in words:
    for i, char in enumerate(word):
        sums[i] += ord(char)
        counts[i] += 1

mean_word = ""
for i in range(max_len):
    if counts[i] > 0:
        mean_char = chr(sums[i] // counts[i])
        mean_word += mean_char
    else:
        mean_word += ""

print(mean_word)
