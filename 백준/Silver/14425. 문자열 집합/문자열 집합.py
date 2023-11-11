import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

str_list = [sys.stdin.readline().rstrip() for _ in range(N)]

cnt = 0

for i in range(M):
    answer = sys.stdin.readline().rstrip()

    if answer in str_list:
        cnt += 1

print(cnt)
