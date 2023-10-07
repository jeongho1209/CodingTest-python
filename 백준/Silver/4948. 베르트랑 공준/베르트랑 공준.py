import math
import sys

while True:
    N = int(sys.stdin.readline().rstrip())

    if N == 0:
        break

    arr = [1, 1] + [0] * (N * 2)

    Max = int(math.sqrt(N * 2))

    cnt = 0

    for i in range(2, Max + 1):  # 2부터 2N까지의 소수를 구할거임
        if arr[i] == 0:  # 소수 판정 안 났으면
            for j in range(i * i, N * 2 + 1, i):  # 2N까지 모두 돌면서 소수가 아니라면 1을 넣어줌
                arr[j] = 1

    for i in range(N + 1, N * 2 + 1):  # 원하는 범위 N ~ 2N까지 봐서
        if arr[i] == 0:
            cnt += 1  # cnt 증가

    print(cnt)