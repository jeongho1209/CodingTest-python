import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    node, edge = map(int, sys.stdin.readline().rstrip().split())

    for _ in range(edge):
        _, _ = map(int, sys.stdin.readline().rstrip().split())

    print(node - 1)
