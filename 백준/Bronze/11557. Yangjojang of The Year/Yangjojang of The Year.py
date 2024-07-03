import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    dic = dict()

    for _ in range(n):
        name, value = sys.stdin.readline().rstrip().split()

        dic[name] = int(value)

    dic1 = sorted(dic.items(), key=lambda x: -x[1])

    print(dic1[0][0])
