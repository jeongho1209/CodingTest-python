import sys

_ = sys.stdin.readline().rstrip()
arr = list(sys.stdin.readline().rstrip())

bonus_score = 0
answer = 0

for index, value in enumerate(arr):
    if value == 'X':
        bonus_score = 0
    else:
        answer += index + 1
        answer += bonus_score
        bonus_score += 1

print(answer)
