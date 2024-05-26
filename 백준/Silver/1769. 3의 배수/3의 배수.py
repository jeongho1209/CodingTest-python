import sys

correct = [3, 6, 9]
cnt = 0

ans = ''

arr = list(map(int, sys.stdin.readline().rstrip()))

if len(arr) == 1:
    print(0)
    if arr[0] in correct:
        print('YES')
    else:
        print('NO')
    exit()

while True:
    ans = str(sum(arr))
    cnt += 1

    arr = []

    for i in ans:
        arr.append(int(i))

    if len(ans) == 1:
        if int(ans) in correct:
            print(cnt)
            print('YES')
            exit()
        else:
            print(cnt)
            print('NO')
            exit()
