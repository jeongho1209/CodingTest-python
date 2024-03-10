import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    dic1 = {}
    dic2 = {}
    k = int(sys.stdin.readline().rstrip())
    key1 = list(sys.stdin.readline().rstrip().split())
    key2 = list(sys.stdin.readline().rstrip().split())
    encrypt = list(sys.stdin.readline().rstrip().split())

    idx = []

    for i in range(k):
        idx.append(key2.index(key1[i]))

    for i in idx:
        print(encrypt[i], end=' ')
