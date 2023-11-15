import sys

_ = sys.stdin.readline().rstrip()

burger = list(map(int, sys.stdin.readline().rstrip().split()))
side = list(map(int, sys.stdin.readline().rstrip().split()))
juice = list(map(int, sys.stdin.readline().rstrip().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
juice.sort(reverse=True)

min_len = min(len(burger), len(side), len(juice))

answer = 0

for i in range(min_len):
    answer += (burger[i] + side[i] + juice[i]) * 0.9

answer += sum(burger[min_len::])
answer += sum(side[min_len::])
answer += sum(juice[min_len::])

print(sum(burger + side + juice))
print(int(answer))
