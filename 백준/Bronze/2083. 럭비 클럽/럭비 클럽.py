import sys

ans = {}

while True:
    name, age, weight = sys.stdin.readline().split()

    if name == '#':
        break

    if int(age) > 17 or int(weight) >= 80:
        ans[name] = 'Senior'
    else:
        ans[name] = 'Junior'

for k, v in ans.items():
    print(k, v)
