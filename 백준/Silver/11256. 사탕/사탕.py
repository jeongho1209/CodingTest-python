import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    J, N = map(int, sys.stdin.readline().rstrip().split())

    arr = []

    for _ in range(N):
        r, c = map(int, sys.stdin.readline().rstrip().split())
        arr.append(r * c)

    arr.sort(reverse=True)

    cnt = 0

    for i in arr:
        if J <= 0:
            print(cnt)
            break
        else:
            J -= i
            cnt += 1
