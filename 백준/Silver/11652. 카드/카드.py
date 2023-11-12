import sys

n = int(sys.stdin.readline().rstrip())
card_dict = {}

for i in range(n):
    card = int(sys.stdin.readline().rstrip())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

result = sorted(card_dict.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
