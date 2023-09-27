import sys

t = int(sys.stdin.readline().rstrip())

# 1! -> 1, 2! -> 1 * 2, 3! -> 1 * 2 * 3
# dp[i] = dp[i - 1] * i

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp = [1]
    for i in range(1, n + 1): # dp[1] = dp[0] * 1, dp[2] = dp[1] * 2
        dp.append(dp[i - 1] * i)

    answer = str(dp[len(dp) - 1]).rstrip('0')
    print(int(answer[len(answer) - 1]))
