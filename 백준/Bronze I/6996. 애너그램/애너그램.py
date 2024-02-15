import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    newA = sorted(list(a))
    newB = sorted(list(b))

    if ''.join(newA) == ''.join(newB):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
