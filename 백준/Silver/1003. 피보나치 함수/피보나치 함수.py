import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())
    answer = [1, 1]
    for i in range(2, N + 1):
        answer.append(answer[i - 1] + answer[i - 2])

    if N == 0:
        print(1, 0)
        continue
    elif N == 1:
        print(0, 1)
        continue

    print(answer[N - 2], answer[N - 1])
