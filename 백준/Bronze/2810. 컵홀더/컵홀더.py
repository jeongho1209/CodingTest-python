import sys

n = int(sys.stdin.readline().rstrip())
people = sys.stdin.readline().rstrip().replace('LL', 'X')

if people.count('X') >= 1:
    print(n - people.count('X') + 1)
else:
    print(n)
