import sys

N = int(sys.stdin.readline().rstrip())

X, Y, R = map(int, sys.stdin.readline().rstrip().split())

internal_cnt = 0
external_cnt = 0

for _ in range(N):  # 직선 입력
    straight = int(sys.stdin.readline().rstrip())
    minus_str = X - R
    plus_str = X + R

    if straight == minus_str or straight == plus_str:
        external_cnt += 1
    elif minus_str < straight < plus_str:
        internal_cnt += 1

print(internal_cnt, external_cnt)
