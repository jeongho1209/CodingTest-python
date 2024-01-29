import sys

n = int(sys.stdin.readline().rstrip())

gomgom = set()
ans = 0

for _ in range(n):
    target = sys.stdin.readline().rstrip()

    if target == 'ENTER':
        gomgom.clear()
    else:
        if target not in gomgom:
            ans += 1
            gomgom.add(target)

print(ans)
