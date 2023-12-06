import sys

target = sys.stdin.readline().rstrip()

answer = ''

for t in target:
    if 65 <= ord(t) <= 90:
        ans = ord(t) + 13
        if ans > 90:
            ans -= 26
        answer += chr(ans)
    elif 97 <= ord(t) <= 122:
        ans = ord(t) + 13
        if ans > 122:
            ans -= 26
        answer += chr(ans)
    else:
        answer += t

print(answer)
