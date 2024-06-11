import sys

n = int(sys.stdin.readline().rstrip())


def fibo1(k):
    a, b = 1, 1
    for _ in range(3, k + 1):
        a, b = b, a + b

    return b


def fibo2(k):
    return k - 2


print(fibo1(n), fibo2(n))
