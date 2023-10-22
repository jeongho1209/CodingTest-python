import sys

arr = []

Max = 0

answerI = 0
answerJ = 0

for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if arr[i][j] > Max:
            Max = arr[i][j]
            answerI = i
            answerJ = j

print(Max)
print(answerI + 1 , answerJ + 1)
