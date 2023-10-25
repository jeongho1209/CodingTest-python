# import sys
#
# answer = {}
#
# for i in range(8):
#     answer[i] = int(sys.stdin.readline().rstrip())
#
# new_answer = sorted(list(answer.values()))
# reverse_answer = dict(map(reversed, answer.items()))
# num_answer = []
#
# for i in new_answer[3:]:
#     if reverse_answer[i]:
#         num_answer.append(reverse_answer[i] + 1)
#
# print(sum(new_answer[3:]))
#
# num_answer.sort()
#
# for i in num_answer:
#     print(i, end=" ")

import sys

answer = []
num_answer = []
max_answer = 0

for _ in range(8):
    answer.append(int(sys.stdin.readline().rstrip()))

for i in range(5):
    maxI = max(answer)
    max_answer += maxI
    maxIndex = answer.index(maxI)
    num_answer.append(maxIndex + 1)
    answer[maxIndex] = 0

num_answer.sort()
print(max_answer)

for i in num_answer:
    print(i, end=" ")
