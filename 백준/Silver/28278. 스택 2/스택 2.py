import sys

stack = []

for _ in range(int(sys.stdin.readline().rstrip())):
    answer = sys.stdin.readline().rstrip().split()

    if answer[0] == '1':
        stack.append(int(answer[1]))
    elif answer[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif answer[0] == '3':
        print(len(stack))
    elif answer[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif answer[0] == '5':
        if stack:
            print(stack[len(stack) - 1])
        else:
            print(-1)
