import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    _, command = sys.stdin.readline().rstrip().split()

    ans = []

    problems = list(sys.stdin.readline().rstrip().split())

    if command == 'C':
        for p in problems:
            ans.append(ord(p) - 64)
    elif command == 'N':
        for p in problems:
            ans.append(chr(int(p) + 64))

    print(*ans)
