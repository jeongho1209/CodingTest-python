import sys

queue = []

for _ in range(int(sys.stdin.readline().rstrip())):
    k = int(sys.stdin.readline().rstrip())
    if k == 0:
        queue.pop()
    else:
        queue.append(k)

print(sum(queue))