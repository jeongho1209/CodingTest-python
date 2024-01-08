import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().rstrip().split())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

dict_nums = defaultdict(int)
ans = 0
start, end = 0, 0

while end < N:
    if dict_nums[numbers[end]] >= K:
        dict_nums[numbers[start]] -= 1
        start += 1
    else:
        dict_nums[numbers[end]] += 1
        end += 1
        ans = max(end - start, ans)

print(ans)
