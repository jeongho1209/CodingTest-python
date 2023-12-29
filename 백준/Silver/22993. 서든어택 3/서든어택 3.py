import sys

_ = int(sys.stdin.readline().rstrip())
wars = list(map(int, sys.stdin.readline().rstrip().split()))

target = wars[0]

answer = 'Yes'

wars = sorted(wars[1:])

for i in wars:
    if target > i:
        target += i
    else:
        answer = 'No'
        break

print(answer)
