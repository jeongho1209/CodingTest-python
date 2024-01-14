import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

stack = [1]

for i in range(1, n):
    stack.insert(i - numbers[i], i + 1)

print(*stack)
