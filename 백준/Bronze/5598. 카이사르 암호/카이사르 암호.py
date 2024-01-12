import sys

word = list(sys.stdin.readline().rstrip())

ans = ''

for i in word:
    target = ord(i) - 3
    if target < ord('A'):
        target += 26
    ans += chr(target)

print(ans)
