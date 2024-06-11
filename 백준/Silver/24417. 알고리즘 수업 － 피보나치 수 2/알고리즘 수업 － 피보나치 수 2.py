import sys

n = int(sys.stdin.readline().rstrip())


def fibo1(k):
    a, b = 1, 1
    for _ in range(3, k + 1):
        a, b = b % 1000000007, (a + b) % 1000000007

    return b


def fibo2(k):
    return k - 2


print(fibo1(n) % 1000000007, fibo2(n) % 1000000007)
