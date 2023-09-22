import sys

S = sys.stdin.readline().rstrip()

answer = [-1] * 26

for i in range(len(S)):
    answer[ord(S[i]) - 97] = S.index(S[i])

for i in answer:
    print(i, end=' ')