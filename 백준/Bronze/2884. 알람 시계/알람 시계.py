A, B = map(int, input().split())

answer = A * 60 + B - 45

h = answer // 60

if answer // 60 < 0:
    h += 24

print(h, answer % 60)
