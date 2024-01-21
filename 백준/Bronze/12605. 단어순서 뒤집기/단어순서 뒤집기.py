import sys

n = int(sys.stdin.readline().rstrip())

words = []

cnt = 1

for _ in range(n):
    words.append(list(sys.stdin.readline().split()))

for word in words:
    target = ''
    word.reverse()
    for i in word:
        target += i
        target += ' '
    print(f'Case #{cnt}: {target.rstrip()}')
    cnt += 1
