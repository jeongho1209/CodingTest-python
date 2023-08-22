# 1. N <= 10000이기 때문에 100까지의 소수만 구해서 배열에 담는다
# 2. 배열을 순회하며 arr[i] * arr[i + 1] -> N보다 클 때 멈추기

N = int(input())

primeNumbers = []


def primeNumber(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for j in range(2, 200):
    if primeNumber(j):
        primeNumbers.append(j)

for index in range(len(primeNumbers)):
    multiplePrimeNum = primeNumbers[index] * primeNumbers[index + 1]
    if multiplePrimeNum > N:
        print(multiplePrimeNum)
        break
