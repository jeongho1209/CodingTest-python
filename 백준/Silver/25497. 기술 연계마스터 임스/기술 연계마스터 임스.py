import sys

_ = sys.stdin.readline()
skills = list(sys.stdin.readline().rstrip())

numbers = [str(i) for i in range(1, 10)]

stack = []

cnt = 0

for skill in skills:
    if skill == 'L' or skill == 'S':
        stack.append(skill)

    if skill in numbers:
        cnt += 1

    if skill == 'R':
        try:
            stack.remove('L')
            cnt += 1
        except:
            break
    if skill == 'K':
        try:
            stack.remove('S')
            cnt += 1
        except:
            break

print(cnt)
