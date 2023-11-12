import sys

dict_answer = {}

answer = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    name, status = sys.stdin.readline().rstrip().split()
    dict_answer[name] = status

for k, v in dict_answer.items():
    if v == 'enter':
        answer.append(k)

answer.sort(reverse=True)

for i in answer:
    print(i)