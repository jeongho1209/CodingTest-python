import sys

while True:
    words = list(sys.stdin.readline().rstrip())
    if words[0] == '#':
        break

    target = ['a', 'e', 'i', 'o', 'u']
    cnt = 0

    for i in words:
        if i.lower() in target:
            cnt += 1

    print(cnt)
