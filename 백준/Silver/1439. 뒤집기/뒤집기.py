import sys

words = sys.stdin.readline().rstrip()
answer = 0

for i in range(len(words) - 1):
    if words[i] != words[i + 1]:
        answer += 1

print((answer + 1) // 2)