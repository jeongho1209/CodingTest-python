import sys

while True:
    a = int(sys.stdin.readline().rstrip())

    if a == 0:
        break

    result = 0

    for i in range(1, a + 1):
        result += i

    print(result)
