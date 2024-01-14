import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

stack = [1]

if numbers[1] == 0:
    stack.append(2)
else:
    stack.insert(0, 2)

for i in range(2, n):
    stack.insert(i - numbers[i], i + 1)

print(' '.join(map(str, stack)))
