import sys

while True:

    N, M = map(int, sys.stdin.readline().rstrip().split())

    if N == 0 and M == 0:
        exit()

    cd1 = set()
    cd2 = set()

    for _ in range(N):
        cd1.add(int(sys.stdin.readline().rstrip()))

    for _ in range(M):
        cd2.add(int(sys.stdin.readline().rstrip()))

    answer = cd1 & cd2
    print(len(answer))
