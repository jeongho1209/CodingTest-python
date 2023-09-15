import sys

N = int(sys.stdin.readline().rstrip())

answer = []
index = []

for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split(" ")
    answer.append([int(age), name])

answer.sort(key=lambda x: x[0])

for a, n in answer:
    print(a, n)
