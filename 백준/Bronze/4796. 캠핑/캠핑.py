import sys

i = 1

while True:
    L, P, V = map(int, sys.stdin.readline().rstrip().split())

    if L == 0 and P == 0 and V == 0:
        break

    ans = V // P  # 2
    answer = L * ans
    answer += min(V % P, L)
    print(f"Case {i}: {answer}")

    i += 1
