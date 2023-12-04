import sys

check = ['U', 'C', 'P', 'C'] + ['1'] * 1000
idx = 0

UCPC = sys.stdin.readline().rstrip()

for i in UCPC:
    if i == check[idx]:
        idx += 1

if idx >= 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
