import sys

n = int(sys.stdin.readline().rstrip())

trops = []

for _ in range(n):
    trops.append(int(sys.stdin.readline().rstrip()))

left_cnt, right_cnt = 1, 1

target = trops[0]

for left in range(len(trops) - 1):
    if target < trops[left + 1]:
        target = trops[left + 1]
        left_cnt += 1

trops.reverse()

target = trops[0]

for right in range(len(trops) - 1):
    if target < trops[right + 1]:
        target = trops[right + 1]
        right_cnt += 1

print(left_cnt)
print(right_cnt)
