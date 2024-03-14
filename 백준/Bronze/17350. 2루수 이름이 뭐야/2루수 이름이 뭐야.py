import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

ans = '뭐야?'

for i in arr:
    if i == 'anj':
        ans = '뭐야;'

print(ans)
