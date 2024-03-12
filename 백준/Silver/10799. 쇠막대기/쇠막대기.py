import sys

sticks = list(sys.stdin.readline().rstrip())

stack = []

ans = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append(sticks[i])
    elif sticks[i] == ')':
        if sticks[i - 1] == '(':
            stack.pop()
            ans += stack.count('(')
        elif sticks[i - 1] == ')':
            ans += 1
            stack.pop()

print(ans)
