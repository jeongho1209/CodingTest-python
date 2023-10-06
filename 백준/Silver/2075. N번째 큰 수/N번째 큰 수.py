import sys, heapq

heap = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in lst:
        if len(heap) < N:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heap[0])