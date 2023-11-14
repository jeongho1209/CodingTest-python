import sys

n = int(sys.stdin.readline().rstrip())

answer_dict = {}

for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book in answer_dict:
        answer_dict[book] += 1
    else:
        answer_dict[book] = 1

result = sorted(answer_dict.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])
