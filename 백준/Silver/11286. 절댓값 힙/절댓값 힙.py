import heapq
import sys

N = sys.stdin.readline().rstrip()

heap = []

for _ in range(int(N)):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        if x > 0:
            heapq.heappush(heap, (x, x))
        else:
            heapq.heappush(heap, (x*-1, x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
