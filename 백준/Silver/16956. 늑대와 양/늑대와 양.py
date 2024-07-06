import sys

r, c = map(int, sys.stdin.readline().rstrip().split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    graph.append(list(input().rstrip()))

flag = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'S':
                    flag = True
                    break

        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if flag:
    print(0)

else:
    print(1)
    for i in graph:
        print(''.join(i))
