N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())
repair = []

for i in range(N - 7):
    for j in range(M - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):
            for o in range(j, j + 8):
                if (k + o) % 2 == 0:
                    if board[k][o] != 'W':
                        w += 1
                    if board[k][o] != 'B':
                        b += 1
                else:
                    if board[k][o] != 'B':
                        w += 1
                    if board[k][o] != 'W':
                        b += 1
        repair.append(w)
        repair.append(b)

print(min(repair))
