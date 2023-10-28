import sys

_ = sys.stdin.readline().rstrip()
card = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0

card.sort(reverse=True)

for i in range(len(card) - 1):
    i = 0
    answer += card[i] + card[i + 1]
    del card[i + 1]

print(answer)
