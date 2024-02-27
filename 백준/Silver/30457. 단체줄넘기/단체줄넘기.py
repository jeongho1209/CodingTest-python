import sys

# heights = [0] + arr + [0]
#

#
# for i in range(1, N + 1):
#     if heights[i] > heights[i - 1] or heights[i] > heights[i + 1]:
#         ans += 1

N = int(sys.stdin.readline().rstrip())

ans = 0

arr = list(map(int, sys.stdin.readline().rstrip().split()))

target_dict = {}

for i in arr:
    if i not in target_dict:
        target_dict[i] = 1
    elif i in target_dict and target_dict[i] < 2:
        target_dict[i] += 1

print(sum(target_dict.values()))
