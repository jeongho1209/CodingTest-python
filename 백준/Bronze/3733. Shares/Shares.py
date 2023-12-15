import sys

while True:
    try:
        n, s = map(int, sys.stdin.readline().rstrip().split())
        print(s // (n + 1))
    except:
        break
