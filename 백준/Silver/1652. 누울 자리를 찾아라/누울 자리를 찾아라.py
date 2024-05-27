import sys

n = int(sys.stdin.readline().rstrip())

room = []

width = 0
length = 0

for _ in range(n):
    room.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    width_len, length_len = 0, 0

    for j in range(n):
        if room[i][j] == '.':
            width_len += 1
        else:
            width_len = 0

        if width_len == 2:
            width += 1

        if room[j][i] == '.':
            length_len += 1
        else:
            length_len = 0

        if length_len == 2:
            length += 1

print(width, length)
