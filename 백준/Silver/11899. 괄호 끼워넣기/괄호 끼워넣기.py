import sys

target = sys.stdin.readline().rstrip()

while '()' in target:
    target = target.replace('()', '')

print(len(target))
