import sys

while True:
    a = sys.stdin.readline().rstrip()
    if a == '.':
        break

    answer = 'yes'
    stack = []

    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'

    if stack:
        answer = 'no'

    print(answer)
