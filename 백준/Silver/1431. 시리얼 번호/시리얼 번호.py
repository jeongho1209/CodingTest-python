import sys


def sum_num(nums):
    result = 0
    for i in nums:
        if i.isdigit():
            result += int(i)
    return result


n = int(sys.stdin.readline().rstrip())

guitars = []

for _ in range(n):
    guitars.append(sys.stdin.readline().rstrip())

guitars.sort(key=lambda x: (len(x), sum_num(x), x))

for i in guitars:
    print(i)
