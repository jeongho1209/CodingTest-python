import sys

N = int(sys.stdin.readline().rstrip())

cow = {}

ans = 0

for _ in range(N):
    cow_num, move = map(int, sys.stdin.readline().rstrip().split())

    if cow_num not in cow:
        cow[cow_num] = move

    if cow[cow_num] != move:
        cow[cow_num] = move
        ans += 1

print(ans)
