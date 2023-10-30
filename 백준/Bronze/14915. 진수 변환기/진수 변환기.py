import sys, string

tmp = string.digits + string.ascii_uppercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


m, n = map(int, sys.stdin.readline().rstrip().split())

print(convert(m, n))
