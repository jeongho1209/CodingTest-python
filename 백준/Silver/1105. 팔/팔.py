import sys

l, k = sys.stdin.readline().rstrip().split()

if len(l) != len(k):
    print(0)
    exit()

cnt = 0

for i in range(len(l)):
    if l[i] != k[i]:
        break
    else:
        if l[i] == '8':
            cnt += 1

print(cnt)
