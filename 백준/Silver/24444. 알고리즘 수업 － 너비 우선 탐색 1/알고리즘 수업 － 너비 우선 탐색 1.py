import sys
from collections import deque

node, edge, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(node + 1)]
visited = [0] * (node + 1)
cnt = 1

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().rstrip().split())
    graph[src].append(dest)
    graph[dest].append(src)

queue = deque([R])
visited[R] = cnt


def bfs():
    global cnt

    while queue:
        curr_node = queue.popleft()
        graph[curr_node].sort()

        for ne_node in graph[curr_node]:
            if visited[ne_node] == 0:
                cnt += 1
                visited[ne_node] = cnt
                queue.append(ne_node)


bfs()

for i in visited[1:]:
    print(i)
