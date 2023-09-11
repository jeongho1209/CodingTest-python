import sys


def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(sys.stdin.readline().rstrip())

solve = []

if n == 0:
    print(0)
else:
    for _ in range(n):
        solve.append(int(sys.stdin.readline().rstrip()))

    avg = roundUp(n * 0.15)

    solve.sort()
    print(roundUp(sum(solve[avg: n - avg]) / len(solve[avg: n - avg])))
