import sys

N = int(sys.stdin.readline().rstrip())

answer = {}

for _ in range(N):
    x = sys.stdin.readline().rstrip()[0]
    if x not in answer:
        answer[x] = 1
    else:
        answer[x] += 1

ans = ''

for k, v in sorted(answer.items()):
    if v >= 5:
        ans += k

if not ans:
    print('PREDAJA')
else:
    print(ans)
