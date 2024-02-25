import sys

M = int(sys.stdin.readline().rstrip())

answer = set()

for _ in range(M):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == 'add':
        answer.add(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) in answer:
            answer.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in answer:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in answer:
            answer.remove(int(command[1]))
        else:
            answer.add(int(command[1]))
    elif command[0] == 'all':
        answer = {x for x in range(1, 21)}
    else:  # case (empty)
        answer = set()
