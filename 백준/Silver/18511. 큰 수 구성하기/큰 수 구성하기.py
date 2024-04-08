import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0


def find(idx, value):
    global ans

    if value != '':
        if int(value) > N:
            return

        if ans <= int(value):
            ans = int(value)
    for i in range(K):
        find(idx + 1, value + str(arr[i]))


find(0, '')

print(ans)
