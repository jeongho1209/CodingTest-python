a = input()

ans = 0

if a[1] == '0':
    print(10 + int(a[2:]))
else:
    print(int(a[0]) + int(a[1:]))
