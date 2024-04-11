import sys

A, P = map(int, sys.stdin.readline().rstrip().split())

D = [A]

target = 0

for i in range(1, 9999):
    SUM = 0
    for j in str(D[i - 1]):
        SUM += pow(int(j), P)
    if SUM in D:
        target = SUM
        break
    D.append(SUM)

print(D.index(target))
