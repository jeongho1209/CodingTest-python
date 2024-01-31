import sys

n = int(sys.stdin.readline().rstrip())

files = {}

for _ in range(n):
    _, extension = sys.stdin.readline().rstrip().split('.')

    if extension in files:
        files[extension] += 1
    else:
        files[extension] = 1

ans = sorted(list(files.items()))

for k, v in ans:
    print(k, v)