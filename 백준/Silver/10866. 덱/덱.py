from collections import deque
import sys

queue = deque()

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push_front":
        queue.appendleft(order[1])  # 덱 앞에 넣기
    elif order[0] == "push_back":
        queue.append(order[1])  # 덱 뒤에 넣기
    elif order[0] == "pop_front":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())  # 덱 앞에서 빼면서 출력
    elif order[0] == "pop_back":
        if not queue:
            print(-1)
        else:
            print(queue.pop())  # 덱 뒤에서 빼면서 출력
    elif order[0] == "size":
        print(len(queue))  # 크기
    elif order[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[len(queue) - 1])
