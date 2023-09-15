T = int(input())

for _ in range(T):
    answer = [1, 1, 1]
    N = int(input())

    for i in range(3, N):
        answer.append(answer[i - 3] + answer[i - 2])

    print(answer[N - 1])
