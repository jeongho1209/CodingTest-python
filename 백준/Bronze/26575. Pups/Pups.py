n = int(input())

for _ in range(n):
    a, b, c = map(float, input().split())

    print('$%.2f' % (a * b * c))
