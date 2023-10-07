import math
import sys

arr = [1, 1] + [0] * 5000000

Max = math.sqrt(5000000)

prime = []

N = int(sys.stdin.readline().rstrip())

for i in range(2, int(Max + 1)):
    if arr[i] == 0:
        for j in range(i * i, 5000000, i):
            arr[j] = 1

for i in range(len(arr)):
    if arr[i] == 0:
        prime.append(i)

print(prime[N - 1])
