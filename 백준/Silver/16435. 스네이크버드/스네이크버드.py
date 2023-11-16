import sys

n, l = map(int, sys.stdin.readline().rstrip().split())

food = list(map(int, sys.stdin.readline().rstrip().split()))
food.sort()

for i in food:
    if l >= i:
        l += 1

print(l)