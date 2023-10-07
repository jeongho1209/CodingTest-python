import math
import sys

_ = sys.stdin.readline().rstrip()
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prime = []


def isPrime(q):
    x = int(math.sqrt(q))
    for j in range(2, x + 1):
        if q % j == 0:
            return False
    return True


def lcm(a, b):
    return a * b // math.gcd(a, b)


def answer(primes):
    while True:
        primes.append(lcm(primes.pop(), primes.pop()))

        if len(primes) == 1:
            return primes[0]


for i in arr:
    if isPrime(i):
        prime.append(i)

if prime:
    print(answer(prime))
else:
    print(-1)
