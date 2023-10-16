import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue_stack = list(map(int, sys.stdin.readline().rstrip().split()))
elements = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
push_elements = list(map(int, sys.stdin.readline().rstrip().split()))

que_stack = deque()

for i in range(n):
    if queue_stack[i] == 0:
        que_stack.append(elements[i])
else:
    if not elements:
        print(push_elements)
        sys.exit()

for i in range(m):
    que_stack.appendleft(push_elements[i])
    print(que_stack.pop(), end=" ")
