import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

answer = [0 for i in range(n + 1)]
for i in range(2, n + 1):
    if answer[i] == 0:
        for t in range(i, n + 1, i):
            answer[t] = i
ans = 0
for i in answer:
    if i <= m:
        ans += 1
print(ans - 1)
