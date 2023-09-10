import sys

from collections import Counter

_ = sys.stdin.readline()
card = list(map(int, sys.stdin.readline().split()))
_ = sys.stdin.readline()
myCard = list(map(int, sys.stdin.readline().split()))

c = Counter(card)

print(' '.join(f'{c[m]}' if m in c else '0' for m in myCard))
