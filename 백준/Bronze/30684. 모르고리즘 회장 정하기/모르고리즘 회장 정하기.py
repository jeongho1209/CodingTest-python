import sys

n = int(sys.stdin.readline().rstrip())

people = []

for _ in range(n):
    target = sys.stdin.readline().rstrip()

    if len(target) == 3:
        people.append(target)

print(sorted(people)[0])
