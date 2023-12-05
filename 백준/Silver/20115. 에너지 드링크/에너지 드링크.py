import sys

_ = sys.stdin.readline().rstrip()
drinks = list(map(int, sys.stdin.readline().rstrip().split()))

drinks.sort(reverse=True)

answer = drinks[0]

for i in range(1, len(drinks)):
    answer += drinks[i] / 2

print(answer)