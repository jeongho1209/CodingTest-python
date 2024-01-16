import sys

cnt = 0
trees = {}

while True:
    tree = sys.stdin.readline().rstrip()

    if tree == '':
        break

    cnt += 1

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

sorted_trees = sorted(trees.items())

for k, v in sorted_trees:
    target = v / cnt * 100
    print("%s %.4f" % (k, target))
