import sys

team_a = list(map(int, sys.stdin.readline().rstrip().split()))
team_b = list(map(int, sys.stdin.readline().rstrip().split()))

a_ans = 0
b_ans = 0

for i in range(5):
    if i == 0:
        a_ans += 6 * team_a[0]
        b_ans += 6 * team_b[0]
    elif i == 1:
        a_ans += 3 * team_a[1]
        b_ans += 3 * team_b[1]
    elif i == 2:
        a_ans += 2 * team_a[2]
        b_ans += 2 * team_b[2]
    elif i == 3:
        a_ans += 1 * team_a[3]
        b_ans += 1 * team_b[3]
    else:
        a_ans += 2 * team_a[4]
        b_ans += 2 * team_b[4]

print(a_ans, b_ans)
