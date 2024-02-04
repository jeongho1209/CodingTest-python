import sys

N, C = map(int, sys.stdin.readline().rstrip().split())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

num_dict = {}

for k, v in enumerate(numbers):
    if v not in num_dict:
        num_dict[v] = [1, k]
    else:
        num_dict[v][0] += 1

num_dict = sorted(num_dict.items(), key=lambda x: (-x[1][0], x[1][1]))
result = []

for k, v in num_dict:
    result += ([str(k)] * v[0])

print(*result)