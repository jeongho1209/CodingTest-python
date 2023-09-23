N, _ = map(int, input().split())

ranks = input().split()

answer = []

for rank in ranks:
    P = (int(rank) * 100) // N

    if 0 <= P <= 4:
        answer.append(1)
    elif 4 < P <= 11:
        answer.append(2)
    elif 11 < P <= 23:
        answer.append(3)
    elif 23 < P <= 40:
        answer.append(4)
    elif 40 < P <= 60:
        answer.append(5)
    elif 60 < P <= 77:
        answer.append(6)
    elif 77 < P <= 89:
        answer.append(7)
    elif 89 < P <= 96:
        answer.append(8)
    elif 96 < P <= 100:
        answer.append(9)

for i in answer:
    print(i, end=' ')
