import sys

N = int(sys.stdin.readline().rstrip())

milks = []

for _ in range(N):
    milks.append(int(sys.stdin.readline().rstrip()))

milks.sort(reverse=True)

ans = 0

for i in range(0, len(milks), 3):
    try:
        ans += milks[i] + milks[i + 1]
    except:
        ans += sum(milks[i:])

print(ans)
