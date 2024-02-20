import sys

N = int(sys.stdin.readline().rstrip())

memos = list(sys.stdin.readline().rstrip())

t_dict = {"B": 0, "S": 0, "A": 0}

for i in range(len(memos)):
    t_dict[memos[i]] += 1

ans = sorted(list(t_dict.items()), key=lambda x: x[1], reverse=True)

t = ans[0][1]
answer = ''
for k, v in ans:
    if v == t:
        answer += k

if answer == 'BSA':
    print('SCU')
else:
    print(answer)
