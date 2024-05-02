import sys

ans = [i for i in range(1, 21)]

for _ in range(10):
    m, n = map(int, sys.stdin.readline().split())
    a = ans[:m - 1]
    b = ans[m - 1:n][::-1]
    c = ans[n:]
    ans = a + b + c

for i in ans:
    print(i, end=' ')
