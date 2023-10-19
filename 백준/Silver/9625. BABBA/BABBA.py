import sys

k = int(sys.stdin.readline().rstrip())

arrA = [1, 0]
arrB = [0, 1]

for i in range(2, k + 1):
    arrA.append(arrA[i - 1] + arrA[i - 2])
    arrB.append(arrB[i - 1] + arrB[i - 2])

print(arrA[k], arrB[k])
