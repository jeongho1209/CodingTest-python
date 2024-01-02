import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    node, edge = map(int, sys.stdin.readline().rstrip().split())

    trees = [[] for _ in range(node + 1)]

    for _ in range(edge):
        src, dest = map(int, sys.stdin.readline().rstrip().split())
        trees[src].append(dest)
        trees[dest].append(src)

    print(node - 1)
