import sys

n = int(sys.stdin.readline().rstrip())

answer = []

for _ in range(n):
    name, day, month, year = sys.stdin.readline().rstrip().split()

    answer.append([int(year), int(month), int(day), name])

answer.sort()

print(answer[len(answer) - 1][3])
print(answer[0][3])