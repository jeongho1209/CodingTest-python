import sys

N = int(sys.stdin.readline().rstrip())

word = list(sys.stdin.readline().rstrip())

ans = [0] * N

for i in range(N):
    value = int(sys.stdin.readline().rstrip())

    ans[i] = value

stack = []

for w in word:
    if 'A' <= w <= 'Z':
        stack.append(ans[ord(w) - ord('A')])
    else:
        value2 = stack.pop()
        value1 = stack.pop()

        if w == '+':
            stack.append(value1 + value2)
        elif w == '-':
            stack.append(value1 - value2)
        elif w == '*':
            stack.append(value1 * value2)
        elif w == '/':
            stack.append(value1 / value2)

print('%.2f' % stack[0])
