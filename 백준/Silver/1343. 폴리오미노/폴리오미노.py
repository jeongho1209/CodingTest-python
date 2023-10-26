import sys

answer = sys.stdin.readline().rstrip()

answer = answer.replace('XXXX', 'AAAA')
answer = answer.replace('XX', 'BB')

if 'X' in answer:
    print(-1)
else:
    print(answer)
