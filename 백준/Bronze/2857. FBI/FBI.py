import sys

fbis = []

for i in range(1, 6):
    fbis.append((i, sys.stdin.readline().rstrip()))

ans = []

for f in fbis:
    if 'FBI' in f[1]:
        ans.append(f[0])

if ans:
    print(' '.join(map(str, ans)))
else:
    print('HE GOT AWAY!')