import math
import sys

t = int(sys.stdin.readline().rstrip())


def isPrime(x):
    if x == 0 or x == 1:
        return False
    for j in range(2, int(math.sqrt(x) + 1)):
        if x % j == 0:
            return False
    return True


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    targets = []

    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1
