T = int(input())


def gcd(a, b):
    answer = []
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            answer.append(i)

    return max(answer)


for _ in range(T):
    a, b = map(int, input().split())

    gcdAnswer = gcd(a, b)

    print(a * b // gcdAnswer, gcd(a, b))
