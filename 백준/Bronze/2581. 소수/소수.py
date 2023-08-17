M = int(input())
N = int(input())

answer = []


def is_prime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True


for i in range(M, N + 1):
    if is_prime(i):
        answer.append(i)

if 1 in answer:
    answer.remove(1)

if len(answer) != 0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
