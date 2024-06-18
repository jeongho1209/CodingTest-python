x, y = input().split()


def reverse(t):
    return t[::-1]


print(int(reverse(str(int(reverse(x)) + int(reverse(y))))))
