import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

answer = {}

for i in range(N):
    k, v = sys.stdin.readline().rstrip().split()
    answer[k] = v

for i in range(M):
    k = sys.stdin.readline().rstrip()
    print(answer[k])
