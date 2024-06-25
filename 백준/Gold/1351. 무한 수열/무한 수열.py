import sys

n, p, q = map(int, sys.stdin.readline().rstrip().split())

dictionary = {0: 1}

if n == 0:
    print(1)
    exit()


def solution(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = solution(n // p) + solution(n // q)
        return dictionary[n]


print(solution(n))
