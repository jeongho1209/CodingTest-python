import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    targets = list(sys.stdin.readline().rstrip())

    stack = []

    ans = 'YES'

    for t in targets:
        if t == '(':
            stack.append(t)
        elif t == ')':
            if stack:
                if stack.pop() != '(':
                    ans = 'NO'
            else:
                ans = 'NO'

    if stack:
        ans = 'NO'

    print(ans)
