num1 = []
num2 = []
for _ in range(3):
    x, y = map(int, input().split())
    num1.append(x)
    num2.append(y)

ans1, ans2 = 0, 0

for i in range(3):
    if num1.count(num1[i]) == 1:
        ans1 = num1[i]
    if num2.count(num2[i]) == 1:
        ans2 = num2[i]

print(ans1, ans2)
