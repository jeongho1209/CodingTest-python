import sys

n = int(sys.stdin.readline().rstrip())

ans = {}
numbers = []

for t in range(n):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    max_num = 0
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                target = (numbers[i] + numbers[j] + numbers[k]) % 10
                if max_num <= target:
                    max_num = target
    ans[t + 1] = max_num

re_ans = {v: k for k, v in ans.items()}

print(re_ans[max(re_ans.keys())])
