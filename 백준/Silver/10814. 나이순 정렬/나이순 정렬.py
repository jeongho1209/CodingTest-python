import sys
N = int(sys.stdin.readline().rstrip())

answer = []
index = []

for i in range(N):
    age, name = map(str, input().split(" "))
    answer.append([int(age), i, name])

answer.sort()

for a, _, n in answer:
    print(a, n)
