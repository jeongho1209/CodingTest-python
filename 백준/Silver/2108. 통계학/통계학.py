# 산술평균 -> round(sum(받은 list) / n(테케 수))
# 중앙값 -> len(list) / 2 - 1
# 범위 -> max - min

import sys

from collections import Counter


def newRound(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(sys.stdin.readline().rstrip())

answer = []

for _ in range(n):
    answer.append(int(sys.stdin.readline().rstrip()))

answer.sort()

c = Counter(answer).most_common()

if sum(answer) < 0:
    print(round(sum(answer) / n))
else:
    print(newRound(sum(answer) / n))
print(answer[len(answer) // 2])

if len(c) > 1 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(max(answer) - min(answer))
